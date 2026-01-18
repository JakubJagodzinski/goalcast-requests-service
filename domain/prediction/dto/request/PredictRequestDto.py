from pydantic import BaseModel


class PredictRequestDto(BaseModel):
    home_team: str
    away_team: str
