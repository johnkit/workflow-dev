import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()

from .workflow import WorkFlow
from .task import Task

_workflow_names = ['neams.1']

def create(name):
    """Initializes workflow with specified name.

    For test & demo use.

    @param name: string identifier, must match _workflow_names
    @return: Workflow object, or None if name not supported
    """

    if name not in _workflow_names:
        print('Sorry, we only support these workflow names: {}'.format(_workflow_names))
        return None

    if name == 'neams.1':
        from . import neams1
        return neams1.create(_session)

    return None

# Initialize engine and session
_engine = create_engine('sqlite:///:memory:', echo=False)
DeclarativeBase.metadata.create_all(_engine)

Session = sessionmaker(bind=_engine)
_session = Session()
