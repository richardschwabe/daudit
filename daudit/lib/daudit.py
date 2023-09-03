import importlib
import sys
import daudit.settings as settings
from daudit.lib.console import console
class DAudit:
    def run(self) -> None:
        """Entrypoint for DAudit
        """
        self.discover_modules()
        self.load_modules()
        for module in settings.LOADED_MODULES:
            module.loader().run()

    def discover_modules(self) -> None:
        """Goes over all the folders for possible modules locations and then
        checks for enabled modules to be loaded.

        The final module list is added to the settings.ENABLED_MODULES list
        """
        for folder in [settings.HOME_MODULES, settings.MODULES_FOLDER]:
            for module_item in folder.glob("*.py"):
                if "__pycache__" in module_item.name:
                    continue
                if not module_item.name.startswith("_"):
                    settings.ENABLED_MODULES.append(module_item)

    def load_modules(self) -> None:
        for module_name in settings.ENABLED_MODULES:
            spec = importlib.util.spec_from_file_location(  # type: ignore
                "module.name", module_name
            )

            module = importlib.util.module_from_spec(spec)  # type: ignore

            sys.modules["module.name"] = module
            spec.loader.exec_module(module)

            # Check if the Module is Valid
            if not hasattr(module, "loader"):
                continue

            settings.LOADED_MODULES.append(module)