from typing import Callable, List
import threading
import time

from win10toast_click import ToastNotifier

from notifier.lib.database import Manga
from notifier.lib.sources.source import Source

class Sentinel:
  
  __threads = []
  __notificator = ToastNotifier()
  
  def __init__(self, watch_interval: int = 3600):
    self.watch_interval = watch_interval
    
  def notify(self, title: str, message: str) -> None:
    if self.__notificator.notification_active():
      time.sleep(10)
    self.__notificator.show_toast(title=title, 
                                  msg=message,
                                  threaded=True)
    
  def spawn_thread(self, callback: Callable[[str], None], *args, **kwargs) -> threading.Thread:
    thread = threading.Thread(target=callback, args=args, kwargs=kwargs)
    thread.start()
    self.__threads.append(thread)
    return thread
  
  def araragi(self, callback: Callable[[str], None], *args, **kwargs):
    while True:
      action_response = callback(*args)
      if isinstance(action_response, Manga) or isinstance(action_response, list):
        self.notify(title=kwargs.get('title', ''), message=kwargs.get('message', ''))
      time.sleep(kwargs.get('custom_interval') or self.watch_interval)
  
  def watch(self, sources: List[Source]):
    for source in sources:
      self.spawn_thread(self.araragi, 
                        source.look_for_new_chapters, 
                        title="New volume is available!", 
                        message=f"A new chapter of {source.plugin.manga_slug.replace('-', ' ')} has been uploaded!\nClick to download.")
    
    self.spawn_thread(self.araragi, 
                      source.look_for_not_downloaded_chapters, 
                      title="You didn't read these yet...", 
                      message="There's some chapters that you didn't downloaded yet. Do you want do it now?",
                      custom_interval=1800)
    
    for thread in self.__threads:
      thread.join()