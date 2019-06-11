import sqlalchemy
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table

from . import DeclarativeBase
from .asset_descriptor import PCEnum

# Association table for workflow.tasks
_task_association = Table('_task_association',
    DeclarativeBase.metadata,
    Column('left_id', Integer, ForeignKey('workflows.id')),
    Column('right_id', Integer, ForeignKey('tasks.id'))
)

# Association table for workflow.assets
# Using class in order to add additional info
class WorkflowAsset(DeclarativeBase):
    __tablename__ = 'workflow_assets'
    left_id = Column(Integer, ForeignKey('workflows.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('asset_descriptors.id'), primary_key=True)
    asset = relationship('AssetDescriptor')
    role = Column(String)
    pc = Column(Enum(PCEnum))


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
    assets = relationship('WorkflowAsset')

    def __repr__(self):
        return 'Workflow {} for Simulation Code {}'.format(
            self.title, self.simulation_code)
