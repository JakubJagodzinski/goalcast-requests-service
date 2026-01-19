from pydantic import BaseModel

from domain.prediction.dto.response.ConfidenceResponseDto import ConfidenceResponseDto


class PredictResponseDto(BaseModel):
    request_id: str
    home_team: str
    away_team: str
    model_name: str
    confidence: ConfidenceResponseDto
    error_occurred: bool
