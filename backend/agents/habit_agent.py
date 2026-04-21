from typing import Dict, Any

class HabitAgent:
    def process(self, state: Dict[str, Any], context: Dict[str, str]) -> Dict[str, Any]:
        """
        Monitor habits, provide nudges based on context and score.
        """
        score = state.get("health_score", 100)
        mood = context.get("mood", "neutral")
        time_of_day = context.get("time_of_day", "day")
        
        insights = []
        
        if score < 50:
            insights.append("You seem to be making a less healthy choice. Try drinking a glass of water first!")
            
        if mood == "stressed":
            insights.append("Stress eating detected. Consider a 5-minute breathing exercise instead of reaching for sugar.")
            
        if time_of_day == "night" and state.get("nutrition", {}).get("carbs", 0) > 50:
            insights.append("Heavy carbs at night can disrupt sleep. Try a lighter protein snack next time.")
            
        if not insights:
            insights.append("Great job keeping your health on track!")
            
        state["habit_insights"] = insights
        return state
