"""
Project Task, which wraps workflow.Task (database TaskAsset)
"""
from workflow.asset_descriptor import PCEnum

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

    def pc(self, asset, as_int=False):
        pc = self._pc_lookup.get(asset)
        if as_int:
            return pc
        # (else)
        return pc.name  # (string)

    def is_ready(self):
        """Return boolean indicating whether prerequiste assets are available.

        Later: return tri-state value to indicate that some sub-tasks are ready
        """
        as_int = True
        for asset in self._assets:
            if bool(self.pc(asset, as_int) & PCEnum.Consumed) and asset.instance is None:
                return False

        # (else) all consumed assets available, so
        return True
