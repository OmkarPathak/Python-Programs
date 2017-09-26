# Author: OMKAR PATHAK
# This is a simple tutorial on usinng SQLAlchemy as ORM (Object Relational Mapping)

# Make sure you have installed SQLAlchemy using: pip3 install sqlalchemy

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


# create a sqlite db
engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    university = Column(String)

    def __init__(self, username, firstname, lastname, university):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.university = university


def create_tables():
    # create tables
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    sqlite_file = 'example.db'
    file_exists = os.path.isfile(sqlite_file)
    if not file_exists:
        create_tables()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create objects
    user = Student('OmkarPathak', 'Omkar', 'Pathak', 'MIT')
    session.add(user)

    # commit the record the database
    session.commit()

    # Select objects
    for student in session.query(Student).order_by(Student.id):
        print (student.firstname, student.lastname)
