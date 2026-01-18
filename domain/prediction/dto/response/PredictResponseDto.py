from pydantic import BaseModel


class PredictResponseDto(BaseModel):
    request_id: str
    home_team: str
    away_team: str
    winner: str
    confidence: float
