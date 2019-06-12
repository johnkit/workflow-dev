"""
Project Asset, which wraps workflow.Asset (database WorkflowAsset)
"""

class Asset:
    def __init__(self, workflow_asset):
        self._workflow_asset = workflow_asset
        self._instance = None    # for smtk resource

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
    def workflow_pc(self, as_int=False):
        pc = self._workflow_asset.pc
        if as_int:
            return pc
        # (else)
        return pc.name  # (string)

    @property
    def instance(self):
        return self._instance

    def set_instance(self, instance):
        self._instance = instance
