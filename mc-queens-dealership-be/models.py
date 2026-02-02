from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, BLOB, ForeignKey, create_engine
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import Optional
from typing import List

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

@dataclass
class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str]  = mapped_column(String(200), nullable=False)
    is_admin: Mapped[Optional[bool]]

    likes: Mapped[List["Like"]] = relationship(cascade='all, delete')

@dataclass
class Car(db.Model):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)
    model: Mapped[str] = mapped_column(String(50), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    fuel_type: Mapped[str] = mapped_column(String(50), nullable=False)
    doors: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[Text] = mapped_column(Text, nullable=False)
    img: Mapped[Optional[BLOB]] = mapped_column(BLOB)
    
    likes: Mapped[List["Like"]] = relationship(cascade='all, delete')


@dataclass
class Like(db.Model):
    __tablename__ = "likes"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id"))