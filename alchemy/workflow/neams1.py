from .workflow import WorkFlow
from .task import Task

def create(session):
    """"""
    # Create workflow object
    workflow = WorkFlow(
        simulation_code='Neutronics',
        title='Neutronics Baseline',
        description='A general RGG-based workflow for demonstration'
        )
    session.add(workflow)

    # Create Tasks
    task1 = Task(title='Specify RGG geometry', description='tbd')
    session.add(task1)
    workflow.tasks.append(task1)

    task2 = Task(title='Specify MCC simulation')
    session.add(task2)
    workflow.tasks.append(task2)

    task3 = Task(title='Generate MCC analysis')
    session.add(task3)
    workflow.tasks.append(task3)

    session.commit()
    return workflow
