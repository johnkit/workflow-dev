"""
Project Task, which wraps workflow.Task (database TaskAsset)
"""

class Task:
    def __init__(self, workflow_task, project_assets, pc_lookup):
        self._workflow_task = workflow_task
        self._assets = project_assets
        self._pc_lookup = pc_lookup  # dict<asset:task_pc>

    @property
    def id(self):
        return self._workflow_task.id

    @property
    def title(self):
        return self._workflow_task.title

    @property
    def description(self):
        return self._workflow_task.description

    @property
    def assets(self):
        return self._assets

    def pc(self, asset):
        return self._pc_lookup.get(asset)
