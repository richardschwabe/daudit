from daudit.lib.models.BaseModule import BaseModule

class CheckIPv4Forwarding(BaseModule):
    title = "CheckIPv4Forwarding"
    description = "Docker should not run with IPv4 Forwarding."

    def check(self):
        client_info = self.client.info()
        if client_info is not None and client_info.get("IPv4Forwarding", False):
            self.add_issue(label="IPv4 Forwarding Enabled", description="Docker daemon reports it is running with automatic IPv4 fowarding.")



loader = CheckIPv4Forwarding