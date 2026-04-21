from typing import Dict, Any

class GroceryAgent:
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert meal plan into structured grocery list.
        """
        meal_plan = state.get("meal_plan", {})
        
        # Basic parsing logic (would be LLM-driven in production)
        grocery_list = [
            {"category": "Produce", "items": ["Berries", "Broccoli", "Asparagus", "Apple", "Mixed vegetables"]},
            {"category": "Proteins", "items": ["Eggs", "Chicken breast", "Salmon", "Paneer"]},
            {"category": "Grains & Pantry", "items": ["Oatmeal", "Quinoa", "Brown rice", "Lentils (Dal)", "Whole wheat bread"]},
            {"category": "Dairy & Nuts", "items": ["Almonds", "Walnuts", "Greek Yogurt"]}
        ]
        
        state["grocery_list"] = grocery_list
        return state
