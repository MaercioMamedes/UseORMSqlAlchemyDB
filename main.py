from database import engine
from models.user import User
from models.address import Address
from models.base import Base
from models.parent import Parent
from models.child import Child
from sqlalchemy.orm import sessionmaker


def main():
    session_class = sessionmaker(bind=engine)
    session = session_class()
    Base.metadata.create_all(engine)
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()

    parent1 = Parent()
    child1 = Child(parent=parent1)
    child2 = Child(parent=parent1)

    session.add_all([parent1, child1, child2])
    session.commit()


if __name__ == "__main__":
    main()
