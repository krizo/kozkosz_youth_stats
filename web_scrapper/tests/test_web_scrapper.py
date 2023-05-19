import pytest

from web_scrapper.match_scraper import MatchScraper


@pytest.fixture
def league_id():
    return 313


def test_web_scrapper(league_id):
    assert len(MatchScraper(league_id).get_matches()) > 0, "Get matches doesn't return any record"
