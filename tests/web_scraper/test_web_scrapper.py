import pytest

from web_scrapper.league_scraper import LeagueScraper
from web_scrapper.matches_scraper import MatchesScraper


@pytest.fixture
def league_id():
    return 313


@pytest.fixture
def leagues_ignored():
    """ League ids for which there is no competition scheduled """
    return [194, 196]


def test_web_scrapper_matches(league_id):
    assert len(MatchesScraper(league_id).get_matches()) > 0, "Get matches doesn't return any record"


def test_web_scraper_leagues():
    assert len(LeagueScraper().get_leagues()) > 0, "Get leagues doesn't return any record"


def test_web_scraper_matches_in_each_league(leagues_ignored):
    for league in LeagueScraper().get_leagues():
        if league.id not in leagues_ignored:
            print(f"Getting matches for league id: {league.id} ({league.name})")
            matches = MatchesScraper(league.id).get_matches()
            print(f"\tFetched {len(matches)} matches")
            assert len(matches) > 0, "Get matches doesn't return any record"

