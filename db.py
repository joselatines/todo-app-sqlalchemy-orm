from sqlalchemy import create_engine,  Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Task(Base):
    __tablename__ = "Tasks"

    id = Column("id", String, primary_key=True, unique=True)
    title = Column("title", String)

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return f"({self.id}, {self.title})"


# connecting to the database
# echo = False => Do not show sql statements
engine = create_engine("sqlite:///my_db.db", echo=False)
Base.metadata.create_all(bind=engine)

# create a session factory for interacting with the database
Session = sessionmaker(bind=engine)
# create a session instance
session = Session()
