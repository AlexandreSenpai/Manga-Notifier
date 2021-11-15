from typing import List
from abc import ABC, abstractmethod

from notifier.lib.crawlers.entities.chapter import Chapter

class SourceInterface(ABC):
  manga_slug: str
  @abstractmethod
  def get_chapter_list(self, manga_slug: str) -> List[Chapter]: pass
  @abstractmethod
  def get_list_of_pages(self, manga_slug: str, chapter: str) -> List[str]: pass