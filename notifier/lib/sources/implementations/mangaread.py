from typing import List
from urllib.parse import urljoin

from notifier.lib.crawlers.scrapper import Scrapper
from notifier.lib.crawlers.entities import Chapter

class MangaRead:
    __BASE_URL = "https://mangaread.co"
    __SOUP = Scrapper.get_soup_instance()
    
    def __init__(self, manga_slug: str) -> None:
        self.manga_slug = manga_slug
    
    def get_chapter_list(self) -> List[Chapter]:
        soup = self.__SOUP(Scrapper.make_request(url=urljoin(self.__BASE_URL, f'/manga/{self.manga_slug}/ajax/chapters/'), method='POST'), 'html.parser')
        
        chapters = soup.find_all('li', class_='wp-manga-chapter')
        
        chapters_list = []
        for chapter in chapters:
            released_date = chapter.find('span', class_='chapter-release-date').find('i').text
            chapter_num = chapter.find('a')
            chapter_url = chapter_num['href']
            
            chapters_list.append(Chapter(chapter=chapter_num.text.strip(),
                                         url=chapter_url,
                                         released_date=released_date))
        
        return chapters_list
    
    def get_list_of_pages(self, chapter: str) -> List[str]:
        soup = self.__SOUP(Scrapper.make_request(urljoin(self.__BASE_URL, f'/manga/{self.manga_slug}/{chapter.replace(".", "-").lower()}/p/1')), 'html.parser')
 
        page_holder = soup.find('select', class_="selectpicker")
        links = page_holder.find_all('option')
        image_pattern = soup.find('img', id='image-0')['data-src']
        image_pattern = image_pattern.split('/')
        
        return links
