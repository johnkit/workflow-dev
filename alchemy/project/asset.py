"""
Project Asset, which wraps workflow.Asset (database WorkflowAsset)
"""

class Asset:
    def __init__(self, workflow_asset):
        self._workflow_asset = workflow_asset

    @property
    def id(self):
        return self._workflow_asset.right_id

    @property
    def asset_type(self):
        return self._workflow_asset.asset.asset_type

    @property
    def description(self):
        return self._workflow_asset.asset.description

    @property
    def workflow_role(self):
        return self._workflow_asset.role

    @property
    def workflow_pc(self):
        return self._workflow_asset.pc
