from .asset import Asset
from .task import Task

class Project:
    def __init__(self, workflow):
        """Placeholder for smtk::project::Project

        """
        self._workflow = workflow
        self._assets = list()
        self._tasks = list()

        # Need table of workflow asset id to project asset
        asset_lookup = dict()  # <asset id, asset>

        for wa in workflow.assets:
            asset = Asset(wa)
            self._assets.append(asset)
            asset_lookup[wa.right_id] = asset


        for wt in workflow.tasks:
            # Retrieve associated project assets
            wa_ids = [wa.right_id for wa in wt.assets]
            assets = [asset_lookup[wa_id] for wa_id in wa_ids]
            pcs = [wa.task_pc for wa in wt.assets]
            pc_lookup = dict(zip(assets, pcs))  # <asset, p/c>

            task = Task(wt, assets, pc_lookup)
            self._tasks.append(task)

    def tasks(self):
        return self._tasks

    def assets(self):
        return self._assets

    def role(self, asset):
        """Returns workflow role for asset"""
        return asset.workflow_role

    def pc(self, asset):
        """Returns workflow P/C info for asset"""
        return asset.workflow_pc

    def assign_asset(self, role, data):
        """Assign asset to project role."""
        for asset in self._assets:
            if asset.workflow_role == role:
                asset.set_instance(data)
                return

        raise RuntimeError('Workflow has no role \"{}\"'.format(role))
