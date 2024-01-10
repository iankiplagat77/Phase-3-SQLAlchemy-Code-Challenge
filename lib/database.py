
from SQLAlchemy import create_engine
from SQLAlchemy.orm import sessionmaker

engine = create_engine('sqlite:///restauran.db')
Session = sessionmaker(bind=engine)
