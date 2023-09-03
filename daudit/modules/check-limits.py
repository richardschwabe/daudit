from daudit.lib.models.BaseModule import BaseModule

class CheckLimits(BaseModule):
    title = "CheckLimits"
    description = "Check for Memory and SWAP limits. These should not be FALSE"

    def check(self):
        client_info = self.client.info()
        if client_info is not None and client_info.get("MemoryLimit") == False:
            self.add_issue(label="MemoryLimit", description="Docker daemon runs without MEMORY limit.")

        if client_info is not None and client_info.get("SwapLimit") == False:
            self.add_issue(label="SWAPLimit", description="Docker daemon runs without SWAP limit.")


loader = CheckLimits