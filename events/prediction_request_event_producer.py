import json
import logging
from datetime import datetime, timezone

from config.kafka.producer.producer import get_kafka_producer

topic: str = "predictions.requests.topic"


async def produce_prediction_request_event(
        request_id: str,
        home_team: str,
        away_team: str,
        model_name: str
):
    logging.info(
        f"Producing prediction request event for {home_team} vs {away_team} (request_id: {request_id}, model_name: {model_name})")

    event_data = {
        "event_type": "PREDICTION_REQUEST",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "request_id": request_id,
        "model_name": model_name,
        "home_team": home_team,
        "away_team": away_team
    }

    logging.info(f"Event data: {event_data}")

    producer = await get_kafka_producer()
    message = json.dumps(event_data)

    await producer.send_and_wait(
        topic,
        value=message,
        headers=[
            ("eventCategory", b"PREDICTION_REQUEST_EVENT"),
            ("eventType", b"PREDICTION_REQUEST")
        ]
    )

    logging.info(
        f"Prediction request event for {home_team} vs {away_team} (request_id: {request_id}, model_name: {model_name}) produced successfully")
