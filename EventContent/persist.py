# mysql connection
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:admin@db.service.consul:3306/contentdb', echo=False, pool_recycle=3600)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Base.query = session.query_property()


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
