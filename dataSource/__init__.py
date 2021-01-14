
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

__all__ = ['Base','session']

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{username}:{password}@{hostname}:{port}/{databasename}?charset=utf8".format(
    username="root",
    password="sm1418!1662",
    hostname="192.168.0.13",
    port="3306",
    databasename="ryutaewan"
)
DATABASES = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

Base = declarative_base

Session = sessionmaker()
Session.configure(bind=DATABASES)
session = Session()

