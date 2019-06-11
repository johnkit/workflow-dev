from .workflow import WorkFlow
from .task import Task
from .asset_descriptor import AssetDescriptor, PCEnum
from .workflow import WorkflowAsset

def create(session):
    """"""
    # Create workflow object
    workflow = WorkFlow(
        simulation_code='Neutronics',
        title='Neutronics Baseline',
        description='A general RGG-based workflow for demonstration'
        )
    session.add(workflow)

    # Create tasks
    task1 = Task(title='Specify RGG geometry', description='tbd')
    session.add(task1)
    workflow.tasks.append(task1)

    task2 = Task(title='Specify MCC simulation')
    session.add(task2)
    workflow.tasks.append(task2)

    task3 = Task(title='Generate MCC analysis')
    session.add(task3)
    workflow.tasks.append(task3)

    # Create assets
    assoc1 = WorkflowAsset(role='reactor_geometry', pc=PCEnum.Produced)
    assoc1.asset = AssetDescriptor(
        workflow=workflow,
        asset_type='smtk::session::rgg::Resource',
        workflow_pc=PCEnum.Produced
    )
    workflow.assets.append(assoc1)

    assoc2 = WorkflowAsset(role='mcc_simulation_spec', pc=PCEnum.Produced)
    assoc2.asset = AssetDescriptor(
        workflow=workflow,
        asset_type='smtk::attribute::Resource',
        workflow_pc=PCEnum.Produced
    )
    workflow.assets.append(assoc2)

    session.commit()
    return workflow
