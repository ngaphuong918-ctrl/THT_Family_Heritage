from .database import Base, engine
from .family import Family
from .person import Person
from .relationship import Relationship


def init_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()
    print("Database initialized successfully.")
