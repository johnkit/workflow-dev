import enum

import sqlalchemy
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.schema import UniqueConstraint

from . import DeclarativeBase


class PCEnum(enum.IntEnum):
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

    # Assets must be unique to a given workflow and role
    UniqueConstraint('workflow', 'role', 'asset_type')

    def __repr__(self):
        return 'Asset type {}'.format(self.asset_type)
