import requests
from bs4 import BeautifulSoup

from utils import wait_until


class WebScraper:
    BASE_URL = 'http://www.kozkosz.pl/'
    _parser = None

    @classmethod
    @wait_until
    def get_page(cls, url: str):
        page = requests.get(cls.BASE_URL + url)
        assert page.text.endswith('</html>')
        return BeautifulSoup(page.content, "html.parser")
