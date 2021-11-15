from dataclasses import dataclass, field

@dataclass
class Chapter:
    chapter: str
    url: str
    released_date: str
    already_seen: int = field(default=0)
