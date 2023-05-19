from dataclasses import dataclass

from bs4 import Tag


@dataclass
class Team:
    id: int
    name: str
    league_id: int
    url: str = None

    @staticmethod
    def create_team_from_cell(link: Tag):
        """ Create Team object based on link element (<a href>)  found on match page.
        Example: <a href="/liga/313/druzyna/d/95/wisla-canpack-krakow.html">Wisła CanPack Kraków</a>
        """
        name = link.text
        team_id = int(link['href'].split('/druzyna/d/')[1].split('/')[0])
        league_id = int(link['href'].split('/liga/')[1].split('/druzyna/')[0])
        url = link['href']
        return Team(name=name, league_id=league_id, url=url, id=team_id)