import datetime
from dataclasses import dataclass

from web_scrapper.models.team import Team


@dataclass
class Match:
    date: datetime.datetime
    home_team: Team
    away_team: Team
    home_score: int
    away_score: int
    url: str
    league_id: int
    completed: bool
