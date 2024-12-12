from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base

#creating base class for our models which is an instance of Base.metadata that allows us to automatically registrate our inherited classes create themselves as db tables
Base = declarative_base()
#creating url in order to connect to db server
url = URL.create (
    drivername = "mysql+mysqlconnector",
    username = "V",
    password = "asxlkm11",
    host = "localhost",
    database = "artdb",
    port = 3306
)
#creating dvijok object with parameters: echo (lets us see all the requests) and pool_pre_ping (checks the connections before starting)
engine = create_engine(url, echo = True, pool_pre_ping = True)
#creating session object without autocommit (in order to commit changes we need to call session.commit()) and autoflush (that means that new changes are invisible unless session.flush() is called)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)