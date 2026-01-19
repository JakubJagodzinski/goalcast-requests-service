from pydantic import BaseModel


class GetAvailableModelsResponseDto(BaseModel):
    models_list: list[str]
