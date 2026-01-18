from pydantic import BaseModel


class GetTeamsResponseDto(BaseModel):
    teams_list: list[str]
