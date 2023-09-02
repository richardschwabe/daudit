import pathlib

import daudit.settings as settings

class DAudit:
    def run(self) -> None:
        self.discover_modules()

    def discover_modules(self):
        for module_item in settings.MODULES_FOLDER.glob("*.*"):
            module_item.name
            print(module_item.name)