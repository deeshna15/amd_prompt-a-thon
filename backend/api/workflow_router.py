from fastapi import APIRouter, Depends
from ..schemas import WorkflowRequest, AgentResponse
from ..agents.nutrition_agent import NutritionAgent
from ..agents.health_agent import HealthAgent
from ..agents.meal_agent import MealAgent
from ..agents.grocery_agent import GroceryAgent
from ..agents.habit_agent import HabitAgent

router = APIRouter()

@router.post("/process", response_model=AgentResponse)
async def process_workflow(request: WorkflowRequest):
    """
    Multi-Agent Workflow Execution
    1. Nutrition Agent -> Extracts foods and gets macros
    2. Health Analyzer -> Computes score
    3. Habit Coach -> Adds coaching context
    4. Meal Planner -> Plans next meals
    5. Grocery Planner -> Generates grocery list
    """
    
    # Base state passed between agents
    state = AgentResponse().dict()

    # Determine input
    food_text = request.input_text
    if request.input_image_base64:
        # Here we would call the Image Analysis Tool
        # For simplicity, simulating image output
        food_text = "Pizza and Cola"
        state["recommendations"].append("Detected items from image.")

    if not food_text:
        return state # Return empty if no input

    # 1. Nutrition Expert Agent
    nutrition_agent = NutritionAgent()
    state = nutrition_agent.process(food_text, state)

    # 2. Health Analyzer Agent
    health_agent = HealthAgent()
    state = health_agent.process(state)

    # 3. Habit Coach Agent (Decision making: only trigger if unhealthy)
    habit_agent = HabitAgent()
    state = habit_agent.process(state, request.context)

    # 4. Meal Planner Agent
    meal_agent = MealAgent()
    state = meal_agent.process(state, request.user_id)

    # 5. Grocery Planner Agent
    grocery_agent = GroceryAgent()
    state = grocery_agent.process(state)

    return state
