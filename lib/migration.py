from SQLAlchemy import create_engine
from SQLAlchemy.orm import sessionmaker
from model import Base, Restaurant, Customer, Review


engine = create_engine('sqlite:///restauran.db')


Base.metadata.bind = engine


Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)


session.commit()
session.close()
