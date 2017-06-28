from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ContentItem(Base):
    __tablename__ = 'ContentItem'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    desc = Column(String(50))

    def __init__(self, event_id=None, desc=None):
        self.event_id = event_id
        self.desc = desc

    def __repr__(self):
        return '<ContentItem %r>' % self.desc
