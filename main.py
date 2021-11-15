from notifier import Notifier, Sentinel
from notifier.lib.sources.implementations.mangaread import MangaRead

notifiers = [Notifier(MangaRead(manga_slug='majime-succubus-hiiragi-san')),
             Notifier(MangaRead(manga_slug='monster-musume-no-iru-nichijou'))]

sentinel = Sentinel()
sentinel.watch(notifiers)