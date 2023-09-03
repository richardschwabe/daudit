from daudit.lib.models.BaseModule import BaseModule

class CheckStorageDriver(BaseModule):
    title = "Storage Mode"
    description = "Docker should have a storage driver."
    def check(self):
        client_info = self.client.info()
        if client_info is not None and client_info.get("Driver", False):
            self.add_issue(label="CheckStorageDriver", description="Docker daemon runs aufs as a storage driver.")



loader = CheckStorageDriver