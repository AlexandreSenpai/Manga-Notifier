from pathlib import Path
from dataclasses import dataclass

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

base = declarative_base()

@dataclass
class Manga(base):
  __tablename__ = 'manga'

  slug: Column = Column(String, primary_key=True)
  chapter: Column = Column(String, primary_key=True)
  url: Column = Column(String, nullable=False, primary_key=True)
  released_date: Column = Column(DateTime, nullable=False)
  downloaded: Column = Column(Boolean, nullable=False, default=False)
  download_date: Column = Column(DateTime, nullable=True)

class Database:
  engine = create_engine(f'sqlite:///{Path.joinpath(Path(__file__).parent.resolve(), "./database.db")}?check_same_thread=False', echo=True)
  session: Session = None

  def __init__(self):
    base.metadata.create_all(self.engine)
    Session = sessionmaker(bind=self.engine)
    
    self.session = Session()
    
  def close(self):
    self.session.close()