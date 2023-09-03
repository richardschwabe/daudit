from daudit.lib.models.BaseModule import BaseModule

class CheckSSHModule(BaseModule):
    def run(self):
        print("CheckSSH")



loader = CheckSSHModule