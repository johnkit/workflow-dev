

class Project:
    def __init__(self, workflow):
        """Placeholder for smtk::project::Project

        """
        self._workflow = workflow

    def tasks(self):
        return self._workflow.tasks

    def assets(self):
        return self._workflow.assets
