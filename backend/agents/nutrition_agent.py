from typing import Dict, Any
import json
import os
import httpx
from google import genai

class NutritionAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=self.api_key) if self.api_key else None
        self.edamam_app_id = os.getenv("EDAMAM_APP_ID")
        self.edamam_app_key = os.getenv("EDAMAM_APP_KEY")

    def process(self, food_text: str, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze food items and return calories, macros.
        Suggests healthier alternatives.
        Uses Edamam API as primary, falls back to LLM.
        """
        # Primary: Edamam API
        if self.edamam_app_id and self.edamam_app_key:
            try:
                # Use synchronous requests for simplicity in this agent method
                response = httpx.get(
                    "https://api.edamam.com/api/nutrition-data",
                    params={"app_id": self.edamam_app_id, "app_key": self.edamam_app_key, "ingr": food_text},
                    timeout=5.0
                )
                if response.status_code == 200:
                    data = response.json()
                    if data.get("calories", 0) > 0:
                        nutrients = data.get("totalNutrients", {})
                        state["nutrition"] = {
                            "calories": round(data.get("calories", 0)),
                            "protein": round(nutrients.get("PROCNT", {}).get("quantity", 0)),
                            "carbs": round(nutrients.get("CHOCDF", {}).get("quantity", 0)),
                            "fat": round(nutrients.get("FAT", {}).get("quantity", 0)),
                            "sugar": round(nutrients.get("SUGAR", {}).get("quantity", 0)),
                            "is_estimated": False
                        }
                        state["food_items"] = [food_text]
                        state["recommendations"].append("Data verified by Edamam.")
                        return state
            except Exception as e:
                print(f"Edamam API Error: {e}")
        
        # Fallback 1: LLM
        if self.client:
            prompt = f"""
            Analyze the following food input: "{food_text}".
            Return a JSON object with:
            - "food_items": list of identified foods
            - "nutrition": {{ "calories": int, "protein": int, "carbs": int, "fat": int, "sugar": int, "is_estimated": true }}
            - "recommendations": list of 2 string tips for healthier alternatives (Indian diet context if applicable)
            Only return the JSON.
            """
            try:
                response = self.client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                text = response.text.replace("```json", "").replace("```", "").strip()
                data = json.loads(text)
                
                state["food_items"] = data.get("food_items", [food_text])
                state["nutrition"] = data.get("nutrition", state["nutrition"])
                state["nutrition"]["is_estimated"] = True # Force it to be true
                state["recommendations"].extend(data.get("recommendations", []))
                return state
            except Exception as e:
                print(f"LLM Error: {e}")
        
        # Fallback 2: Hardcoded
        state["food_items"] = [food_text]
        if "pizza" in food_text.lower():
            state["nutrition"] = {"calories": 800, "protein": 30, "carbs": 90, "fat": 35, "sugar": 10, "is_estimated": True}
            state["recommendations"].append("Consider a whole wheat crust pizza with more veggies.")
        else:
            state["nutrition"] = {"calories": 400, "protein": 20, "carbs": 50, "fat": 15, "sugar": 5, "is_estimated": True}
            state["recommendations"].append("Try adding a side salad to your meal.")
            
        return state
