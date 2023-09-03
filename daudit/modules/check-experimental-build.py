from daudit.lib.models.BaseModule import BaseModule

class CheckExperimentalBuild(BaseModule):
    title = "CheckExperimentalBuild"
    description = "Docker should not run in Experimental Build"

    def check(self):
        client_info = self.client.info()
        if client_info is not None and client_info.get("ExperimentalBuild", False):
            self.add_issue(label="Experimental Mode Enabled", description="Docker daemon runs in ExperimentalBuild.")



loader = CheckExperimentalBuild