from sqlalchemy import Column, Integer, String, Float, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from .database import Base

class UserProfile(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    weight = Column(Float)
    goal = Column(String) # weight loss, maintenance, weight gain
    diet_type = Column(String) # veg, non-veg, keto, etc.
    allergies = Column(JSON) # list of allergies
    current_streak = Column(Integer, default=0)
    highest_streak = Column(Integer, default=0)

class FoodHistory(Base):
    __tablename__ = "food_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    food_items = Column(JSON) # list of foods
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)
    sugar = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class HealthScore(Base):
    __tablename__ = "health_scores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Float)
    reason = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
