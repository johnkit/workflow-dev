import enum

import sqlalchemy
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.schema import UniqueConstraint

from . import DeclarativeBase


class PCEnum(enum.Enum):
    """PC indicates whether assets is Produced and/or Consumed"""
    Consumed = 1
    Produced = 2
    ProducedAndConsumed = 3
    Both = 3


class AssetDescriptor(DeclarativeBase):
    """Public interface to workflow asset descriptors

    Assets have relationships in workflow and task entities
    """
    __tablename__ = 'asset_descriptors'

    id = Column(Integer, primary_key=True)
    workflow = ForeignKey('workflows.id')
    description = Column(String)
    asset_type = Column(String)  # file, folder, smtk::model::Resource, ...
    workflow_pc = Column(Enum(PCEnum))

    UniqueConstraint('workflow', 'role', 'asset_type', 'workflow_pc')

    def __repr__(self):
        return 'Asset type {}'.format(self.asset_type)
