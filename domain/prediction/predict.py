import asyncio
import logging
import uuid

from domain.models.PredictionModelType import PredictionModelType
from domain.prediction.dto.request.PredictRequestDto import PredictRequestDto
from domain.prediction.dto.response.ConfidenceResponseDto import ConfidenceResponseDto
from domain.prediction.dto.response.PredictResponseDto import PredictResponseDto
from domain.teams.teams import get_random_team
from events import prediction_request_event_producer
from state import pending_requests


def prepare_prediction_request(request_dto: PredictRequestDto):
    model_name = request_dto.model_name if request_dto and request_dto.model_name else PredictionModelType.get_random()

    home_team = request_dto.home_team if request_dto and request_dto.home_team else get_random_team()

    away_team = request_dto.away_team if request_dto and request_dto.away_team else None
    while away_team is None or away_team == home_team:
        away_team = get_random_team()

    return model_name, home_team, away_team


async def handle_prediction_request(request_dto: PredictRequestDto) -> PredictResponseDto:
    logging.info(f"Received prediction request: {request_dto}")

    model_name, home_team, away_team = prepare_prediction_request(request_dto)

    request_id = str(uuid.uuid4())

    await prediction_request_event_producer.produce_prediction_request_event(
        request_id=request_id,
        model_name=model_name,
        home_team=home_team,
        away_team=away_team
    )

    loop = asyncio.get_event_loop()
    future = loop.create_future()
    pending_requests[request_id] = future

    result = await future
    await pending_requests.pop(request_id, None)

    confidence = ConfidenceResponseDto(
        home_team_win=result.get("home_team_win"),
        away_team_win=result.get("away_team_win"),
        draw=result.get("draw"),
    )

    response_dto = PredictResponseDto(
        request_id=request_id,
        model_name=result.get("model_name"),
        home_team=result.get("home_team"),
        away_team=result.get("away_team"),
        confidence=confidence,
        error_occurred=result.get("error_occurred"),
    )

    return response_dto
