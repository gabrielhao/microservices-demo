from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EventItem(Base):
    __tablename__ = 'EventItem'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))

    def __init__(self, title=None):
        self.title = title

    def __repr__(self):
        return '<EventItem %r>' % (self.title)