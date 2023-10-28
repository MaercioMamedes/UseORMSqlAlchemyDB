from database import engine
from models.user import User
from models.address import Address
from models.base import Base
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


if __name__ == "__main__":
    main()
