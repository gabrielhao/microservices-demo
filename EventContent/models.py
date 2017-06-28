from sqlalchemy import Column, Integer, String
from persist import Base

class ContentItem(Base):
    __tablename__ = 'ContentItem'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    desc = Column(String(100))

    def __init__(self, event_id, desc):
        self.event_id = event_id
        self.desc = desc

    def __repr__(self):
        return '<ContentItem %r>' % self.desc
