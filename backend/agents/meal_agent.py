from typing import Dict, Any

class MealAgent:
    def process(self, state: Dict[str, Any], user_id: int) -> Dict[str, Any]:
        """
        Generate daily meal plans based on goal and diet type.
        """
        # In a real app, fetch user preferences from DB using user_id
        goal = "weight loss"
        diet_type = "veg"
        
        # Simple simulated generation based on goal
        if diet_type == "veg":
            meal_plan = {
                "breakfast": "Oatmeal with almonds and berries",
                "lunch": "Quinoa salad with chickpeas and paneer",
                "dinner": "Lentil soup (Dal) with mixed vegetables",
                "snacks": ["Apple", "Greek Yogurt"]
            }
        else:
            meal_plan = {
                "breakfast": "Scrambled eggs with whole wheat toast",
                "lunch": "Grilled chicken with brown rice and broccoli",
                "dinner": "Baked salmon with asparagus",
                "snacks": ["Handful of walnuts", "Protein shake"]
            }
            
        state["meal_plan"] = meal_plan
        return state
