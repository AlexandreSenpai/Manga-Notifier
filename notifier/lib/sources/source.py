from typing import List
from datetime import datetime

from notifier.lib.database import Database, Manga
from notifier.lib.sources.interface import SourceInterface

class Source:
  def __init__(self, plugin: SourceInterface) -> None:
    self.plugin = plugin
    self.database = Database().session
    
  def look_for_new_chapters(self) -> Manga:
    last_chapter = sorted(self.plugin.get_chapter_list(), key=lambda x: x.chapter, reverse=True)[0]
    chapters = self.database.query(Manga).filter_by(slug=self.plugin.manga_slug,
                                                    chapter=last_chapter.chapter).all()
    if len(chapters) == 0:
      new_chapter = Manga(slug=self.plugin.manga_slug,
                          chapter=last_chapter.chapter,
                          url=last_chapter.url,
                          released_date=datetime.strptime(last_chapter.released_date, '%Y-%m-%d'))
      self.database.add(new_chapter)
      self.database.commit()

      return new_chapter

  def look_for_not_downloaded_chapters(self) -> List[Manga]:
    return self.database.query(Manga).filter_by(downloaded=False).all()