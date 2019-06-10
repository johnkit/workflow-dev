# From https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# Activate venv/sqlalchemy

import sqlalchemy
print(sqlalchemy.__version__)

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

User.__table__
Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='Eddyman')
print(ed_user.name)
print(ed_user.nickname)
print(ed_user.id)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)

print(ed_user is our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

ed_user.nickname = 'eddie'

print(session.dirty)
print(session.new)
session.commit()

print(ed_user.id)
