import sqlalchemy
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table

from . import DeclarativeBase

# Association table for workflow.tasks
_task_association = Table('_task_association',
    DeclarativeBase.metadata,
    Column('left_id', Integer, ForeignKey('workflows.id')),
    Column('right_id', Integer, ForeignKey('tasks.id'))
)


class WorkFlow(DeclarativeBase):
    """Public interface to workflows"""
    __tablename__ = 'workflows'

    id = Column(Integer, primary_key=True)
    # Todo simulation code/family should be another table
    # i.e., Column should be a ForeighKey('simulation_codes.id')
    # Also: consider renaming to simulation_family?
    simulation_code = Column(String, unique=True)
    title = Column(String)
    description = Column(String)
    tasks = relationship('Task', secondary=_task_association)

    def __repr__(self):
        return 'Workflow {} for Simulation Code {}'.format(
            self.title, self.simulation_code)
