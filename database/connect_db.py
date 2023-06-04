from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = "postgresql+psycopg2://postgres:12345678@localhost:6543/postgres"
engine = create_engine(url)
DBsession = sessionmaker(bind=engine)
session = DBsession()

