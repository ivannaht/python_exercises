from sqlalchemy.orm import Session
from sqlalchemy import select
from tasks_with_sql.sql_create_tables import engine
from tasks_with_sql.sql_orm import User, Address, Country

with Session(engine) as session:
    spongebob = User(
        username="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        username="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(username="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()


session = Session(engine)
stmt = select(User).where(User.username=='patrick')
stmt = select(User)

for user in session.scalars(stmt):
    print(user)

session = Session(engine)
stmt = select(Country)
for country in session.scalars(stmt):
    print(country)
