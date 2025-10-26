from fastapi import FastAPI
from pydantic import BaseModel
from enum import IntEnum


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


@app.post("/send_player_stats")
def send_player_stats(player_stats: PlayerStats) -> DifficultyLevels:
    targetSize: DifficultyLevel
    targetLifeSpan: DifficultyLevel
    
    if player_stats.accuracy < 0.5:
        targetSize = DifficultyLevel.EASY
    elif player_stats.accuracy > 0.9:
        targetSize = DifficultyLevel.HARD
    else:
        targetSize = DifficultyLevel.NORMAL
        
        
    if player_stats.reactionTimeRatio < 0.2:
        targetLifeSpan = DifficultyLevel.HARD
    elif player_stats.reactionTimeRatio > 0.8:
        targetLifeSpan = DifficultyLevel.EASY
    else:
        targetLifeSpan = DifficultyLevel.NORMAL
    
    
    difficulty_levels = DifficultyLevels(
        targetSize,
        targetLifeSpan
    )
    return difficulty_levels

    
@app.get("/test_connection")
def test_connection() -> None:
    return

