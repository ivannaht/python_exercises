from sqlalchemy import Column, Integer, String, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, Mapped, mapped_column
from sqlalchemy.orm import declarative_base
from typing import List
from typing import Optional

from tasks_with_sql.sql_create_tables import engine

Session = sessionmaker(bind=engine)
Base = declarative_base()


class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255))
    code = Column(Unicode(255))
    data = relationship("Data", back_populates="country")


class Indicator(Base):
    __tablename__ = 'indicators'
    id = Column(Unicode(255), primary_key=True)
    name = Column(Unicode(255))
    data = relationship("Data", back_populates="indicator")


class Data(Base):
    __tablename__ = 'data'
    country_id = Column(Integer, ForeignKey('countries.id'), primary_key=True)
    indicator_id = Column(Unicode(255), ForeignKey('indicators.id'), primary_key=True)
    data = Column(UnicodeText)
    country = relationship("Country", back_populates="data")
    indicator = relationship("Indicator", back_populates="data")
    Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = 'user_account'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, username={self.username!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = 'address'
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
