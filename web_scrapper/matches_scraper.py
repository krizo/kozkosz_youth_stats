import datetime

from utils import wait_until
from web_scrapper.models.league import League
from web_scrapper.models.match import Match
from web_scrapper.models.season import Season
from web_scrapper.models.team import Team
from web_scrapper.web_scraper import WebScraper
from bs4 import BeautifulSoup, Tag


class MatchesScraper:
    def __init__(self, league_id: int):
        self.league_id = league_id
        self._league = None
        self._page = None

    @property
    def league(self):
        if self._league is None:
            league_name = self.page.find('button', class_='more-game').text
            self._league = League(id=self.league_id, name=league_name)
        return self._league

    @property
    def page(self) -> BeautifulSoup:
        if self._page is None:
            self._page = WebScraper.get_page(f"liga/{self.league_id}/terminarz_i_wyniki.html")
        return self._page

    def get_matches(self):
        return [self._get_match_from_tr(match_row) for match_row in self.page.find_all('tr', class_='box')]

    @wait_until(timeout=10)
    def _get_match_from_tr(self, tr_element: Tag):
        cells = tr_element.find_all('td')
        try:
            date = datetime.datetime.strptime(cells[0].text, "%d.%m.%Y %H:%M")
            season = Season.get_season_by_date(date)
        except ValueError:
            date = None
            season = None
        home_team = Team.create_team_from_cell(cells[1].find('a'))
        away_team = Team.create_team_from_cell(cells[1].find_all('a')[1])
        match_href = cells[2].find('a')
        score = match_href.text.strip()
        match_url = match_href['href']
        if score == '--:--':
            home_score, away_score, completed = None, None, False
        else:
            home_score, away_score = [int(sc) for sc in score.split(':')]
            completed = True
        return Match(date=date, home_team=home_team, away_team=away_team, home_score=home_score,
                     away_score=away_score, url=match_url, league_id=self.league_id, completed=completed, season=season)
