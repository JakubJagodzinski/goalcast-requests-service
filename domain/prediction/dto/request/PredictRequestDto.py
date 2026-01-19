from pydantic import BaseModel


class PredictRequestDto(BaseModel):
    model_name: str | None = None
    home_team: str | None = None
    away_team: str | None = None
