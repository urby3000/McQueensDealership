from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.orm import declarative_base

db_url = "mysql+pymysql://root:admin@localhost:3306/mc-queens-dealership"

engine = create_engine(db_url)

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    brand = Column(String(50))
    model = Column(String(50))
    year = Column(Integer)


#Base.metadata.create_all(engine)