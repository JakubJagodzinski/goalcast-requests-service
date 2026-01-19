from pathlib import Path

from domain.teams.dto.response.GetTeamsResponseDto import GetTeamsResponseDto


async def get_teams() -> GetTeamsResponseDto:
    teams_list = load_teams()

    response_dto = GetTeamsResponseDto(
        teams_list=teams_list
    )

    return response_dto


TEAMS_FILE_PATH = Path(__file__).parent / "teams.csv"

_TEAMS_CACHE: list[str] | None = None


def load_teams() -> list[str]:
    global _TEAMS_CACHE

    if _TEAMS_CACHE is None:
        with open(TEAMS_FILE_PATH, "r", encoding="utf-8") as file:
            _TEAMS_CACHE = [
                line.strip()
                for line in file
                if line.strip()
            ]

    return _TEAMS_CACHE
