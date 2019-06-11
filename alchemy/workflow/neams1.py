from .asset_descriptor import AssetDescriptor, PCEnum
from .task import Task, TaskAsset
from .workflow import WorkFlow, WorkflowAsset

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
    workflow.tasks.append(task1)

    task2 = Task(title='Specify MCC simulation')
    workflow.tasks.append(task2)

    task3 = Task(title='Generate MCC analysis')
    workflow.tasks.append(task3)

    session.add_all([task1, task2, task3])

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

    assoc3 = WorkflowAsset(role='mcc_simulation_input', pc=PCEnum.Produced)
    assoc3.asset = AssetDescriptor(
        workflow=workflow,
        asset_type='file',
        workflow_pc=PCEnum.Produced
    )
    workflow.assets.append(assoc3)


    # Assign assets to tasks
    geom_produced = TaskAsset(task_pc=PCEnum.Produced, workflow_asset=assoc1)
    task1.assets.append(geom_produced)

    geom_consumed = TaskAsset(task_pc=PCEnum.Consumed, workflow_asset=assoc1)
    task2.assets.append(geom_consumed)
    mcc_atts_produced = TaskAsset(task_pc=PCEnum.Produced, workflow_asset=assoc2)
    task2.assets.append(mcc_atts_produced)

    geom_consumed3 = TaskAsset(task_pc=PCEnum.Consumed, workflow_asset=assoc1)
    task3.assets.append(geom_consumed3)
    mcc_atts_consumed = TaskAsset(task_pc=PCEnum.Consumed, workflow_asset=assoc2)
    task3.assets.append(mcc_atts_consumed)

    mcc_sim_input = TaskAsset(task_pc=PCEnum.Produced, workflow_asset=assoc3)
    task3.assets.append(mcc_sim_input)

    session.commit()
    return workflow
