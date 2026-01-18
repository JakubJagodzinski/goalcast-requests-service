import asyncio
import json
import logging

from config.kafka.consumer.consumer import get_kafka_consumer
from state import pending_requests

topic: str = "predictions.responses.topic"


async def consume_prediction_response_events():
    consumer = await get_kafka_consumer(topic)

    try:
        async for msg in consumer:
            data = json.loads(msg.value)
            request_id = data.get("request_id")
            if request_id in pending_requests:
                pending_requests[request_id].set_result(data)
                logging.info(f"Delivered prediction result: {data}")
    except asyncio.CancelledError:
        pass
    finally:
        await consumer.stop()
