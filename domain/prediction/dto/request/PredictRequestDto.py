from pydantic import BaseModel


class PredictRequestDto(BaseModel):
    model_name: str | None = None
    home_team: str
    away_team: str
