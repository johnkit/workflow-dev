import sqlalchemy
from sqlalchemy import Column, Integer, String

from . import DeclarativeBase

class Task(DeclarativeBase):
    """Public interface to workflow tasks"""
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    def __repr__(self):
        return 'Task {}'.format(self.title)
