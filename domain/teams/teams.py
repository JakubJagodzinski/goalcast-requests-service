from domain.teams.dto.response.GetTeamsResponseDto import GetTeamsResponseDto


async def get_teams() -> GetTeamsResponseDto:
    teams_list = load_teams()

    response_dto = GetTeamsResponseDto(
        teams_list=teams_list
    )

    return response_dto


def load_teams() -> list[str]:
    return [
        "Russia",
        "Poland",
        "Germany",
        "Australia",
        "France",
        "England",
        "Spain",
        "Netherlands"
    ]
