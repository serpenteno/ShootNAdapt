from fastapi import FastAPI
from pydantic import BaseModel
from enum import IntEnum
import joblib


app = FastAPI(title="ShootNAdapt")


class PlayerStats(BaseModel):
    accuracy: float
    reactionTimeRatio: float
    

class DifficultyLevel(IntEnum):
    EASY = 0
    NORMAL = 1
    HARD = 2
   
    
class DifficultyLevels(BaseModel):
    targetSize: DifficultyLevel
    targetLifeSpan: DifficultyLevel
    
    def __init__(self, targetSize: DifficultyLevel, targetLifeSpan: DifficultyLevel) -> None:
        super().__init__(targetSize=targetSize, targetLifeSpan=targetLifeSpan)
        self.targetSize = targetSize
        self.targetLifeSpan = targetLifeSpan


model_target_size = joblib.load("model_target_size.pkl")
model_target_life_span = joblib.load("model_target_life_span.pkl")

@app.post("/send_player_stats")
def send_player_stats(player_stats: PlayerStats) -> DifficultyLevels:
    X_accuracy = [[player_stats.accuracy]]
    X_reaction_time_ratio = [[player_stats.reactionTimeRatio]]
    
    predicted_target_size = int(model_target_size.predict(X_accuracy)[0])
    predicted_target_life_span = int(model_target_life_span.predict(X_reaction_time_ratio)[0])
    
    return DifficultyLevels(
        targetSize=predicted_target_size,
        targetLifeSpan=predicted_target_life_span
    )

    
@app.get("/test_connection")
def test_connection() -> None:
    return

