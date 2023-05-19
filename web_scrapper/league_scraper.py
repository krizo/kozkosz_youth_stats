from bs4 import BeautifulSoup

from web_scrapper.models.league import League
from web_scrapper.types.league_types import LeagueTypes
from web_scrapper.web_scraper import WebScraper


class LeagueScraper:
    _supported_types = LeagueTypes

    def __init__(self, league_type: LeagueTypes = LeagueTypes.KOBIECE):
        self._page = None
        self.type = league_type

    @property
    def page(self) -> BeautifulSoup:
        if self._page is None:
            self._page = WebScraper.get_page('/kluby.html')
        return self._page

    def get_leagues(self) -> [League]:
        leagues = []
        league_sub_menu_root = self.page.find('a', text=str(self.type.value)).parent
        leagues_links = league_sub_menu_root.find_all('a')[1:]
        for li_element in leagues_links:
            link = li_element['href']
            id = int(link.split('liga/')[1].split('.html')[0])
            name = li_element.text
            leagues.append(League(id=id, name=name))
        return leagues


