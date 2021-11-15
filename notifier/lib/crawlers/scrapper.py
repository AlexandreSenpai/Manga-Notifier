from bs4 import BeautifulSoup
from requests import request

class Scrapper:
    @staticmethod
    def make_request(url: str, method: str = 'get', **kwargs) -> bytes:
        response = request(method=method, url=url, **kwargs)
        if response.status_code == 200:
            return response.content
    
    @staticmethod
    def get_soup_instance() -> BeautifulSoup:
        return BeautifulSoup