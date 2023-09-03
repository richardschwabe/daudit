from daudit.lib.models.BaseModule import BaseModule

class CheckSSHModule(BaseModule):
    title = "SSH Enabled"
    description = "Should not run SSH service"

    def check(self):
        ...



loader = CheckSSHModule