from pydantic import BaseModel


class ConfidenceResponseDto(BaseModel):
    home_team_win: float
    away_team_win: float
    draw: float
