from typing import Dict, Any

class HealthAgent:
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compute a dynamic health score (0-100) based on nutrition.
        """
        nutrition = state.get("nutrition", {})
        calories = nutrition.get("calories", 0)
        sugar = nutrition.get("sugar", 0)
        protein = nutrition.get("protein", 0)

        # Basic scoring algorithm
        score = 100
        explanation = []

        if calories > 600:
            score -= 20
            explanation.append("High calorie intake for a single meal.")
        elif calories < 200:
            score -= 10
            explanation.append("Very low calorie intake, might not be filling.")
            
        if sugar > 15:
            score -= 25
            explanation.append(f"High sugar content ({sugar}g).")
            
        if protein > 20:
            score += 10
            explanation.append("Good amount of protein.")
            
        # Bounds check
        score = max(0, min(100, score))
        
        state["health_score"] = score
        state["health_explanation"] = " ".join(explanation) if explanation else "Balanced meal."
        
        return state
