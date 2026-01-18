import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from domain.prediction.dto.request.PredictRequestDto import PredictRequestDto
from domain.prediction.dto.response.PredictResponseDto import PredictResponseDto
from domain.prediction.predict import handle_prediction_request
from domain.teams.dto.response.GetTeamsResponseDto import GetTeamsResponseDto
from domain.teams.teams import get_teams
from events.prediction_response_event_consumer import consume_prediction_response_events

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.consumer_task = asyncio.create_task(consume_prediction_response_events())
    logging.info("Consumer task started")

    try:
        yield
    finally:
        logging.info("Shutting down consumer task")
        app.state.consumer_task.cancel()
        try:
            await app.state.consumer_task
        except asyncio.CancelledError:
            pass


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"status": "healthy"}


@app.get("/api/v1/teams", response_model=GetTeamsResponseDto)
async def get_teams_endpoint():
    response_dto = await get_teams()

    return response_dto


@app.post("/api/v1/predict", response_model=PredictResponseDto)
async def predict_endpoint(
        request_dto: PredictRequestDto
):
    response_dto = await handle_prediction_request(request_dto)

    return response_dto
