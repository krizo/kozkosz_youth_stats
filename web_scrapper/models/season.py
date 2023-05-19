import datetime
from dataclasses import dataclass


@dataclass
class Season:
    year_start: int
    year_end: int

    def __str__(self):
        return f"{self.year_start}/{self.year_end}"

    @staticmethod
    def get_season_by_date(date: datetime.datetime):
        if date.month > 8:
            return Season(year_start=int(date.year), year_end=int(date.year + 1))
        else:
            return Season(year_start=int(date.year - 1), year_end=int(date.year))
