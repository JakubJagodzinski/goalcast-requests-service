from domain.models.PredictionModelType import PredictionModelType
from domain.models.dto.response.GetAvailableModelsResponseDto import GetAvailableModelsResponseDto


async def get_available_models() -> GetAvailableModelsResponseDto:
    models_list = PredictionModelType.get_list()

    response_dto = GetAvailableModelsResponseDto(
        models_list=models_list
    )

    return response_dto
