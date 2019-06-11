import sqlalchemy
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from . import DeclarativeBase
from .asset_descriptor import PCEnum

# Association table for task.assets.
# Used to assign workflow assets to tasks.
# Using class in order to add additional column (task PC)
class TaskAsset(DeclarativeBase):
    __tablename__ = 'task_assets'
    left_id = Column(Integer, ForeignKey('tasks.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('workflow_assets.right_id'), primary_key=True)
    workflow_asset = relationship('WorkflowAsset')
    task_pc = Column(Enum(PCEnum))


class Task(DeclarativeBase):
    """Public interface to workflow tasks"""
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    assets = relationship('TaskAsset')

    def __repr__(self):
        return 'Task {}'.format(self.title)
