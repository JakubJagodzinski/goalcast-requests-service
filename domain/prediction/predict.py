import asyncio
import logging
import uuid

from domain.prediction.dto.request.PredictRequestDto import PredictRequestDto
from domain.prediction.dto.response.PredictResponseDto import PredictResponseDto
from events import prediction_request_event_producer
from state import pending_requests


async def handle_prediction_request(request_dto: PredictRequestDto) -> PredictResponseDto:
    logging.info(f"Received prediction request: {request_dto}")

    request_id = str(uuid.uuid4())

    await prediction_request_event_producer.produce_prediction_request_event(
        request_id=request_id,
        home_team=request_dto.home_team,
        away_team=request_dto.away_team
    )

    loop = asyncio.get_event_loop()
    future = loop.create_future()
    pending_requests[request_id] = future

    result = await future
    await pending_requests.pop(request_id, None)

    response_dto = PredictResponseDto(
        request_id=request_id,
        home_team=result.get("home_team"),
        away_team=result.get("away_team"),
        winner=result.get("winner"),
        confidence=result.get("confidence")
    )

    return response_dto
