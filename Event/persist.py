# mysql connection
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('mysql://root:admin@eventdb.service.consul:3306/eventdb', echo=False, pool_recycle=3600)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

#Session = sessionmaker(bind=engine)
#session = Session()

Base = declarative_base()
Base.query = session.query_property()



#Base.query = session.query_property()


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
