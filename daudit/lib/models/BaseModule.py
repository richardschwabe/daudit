from daudit.lib.console import console
from daudit.lib.models.Issue import Issue


class BaseModule:
    client = None
    title: str = ""
    description: str = ""
    _issues: list[Issue] = list()

    def __init__(self, docker_client) -> None:
        self.client = docker_client
        self._issues = list()

    def success(self, msg):
        console.print(f"[green]{msg}[/green]")

    def warning(self, msg):
        console.print(f"[yellow]{msg}[/yellow]")

    def error(self, msg):
        console.print(f"[red][bold]{msg}[/bold][/red]")

    def info(self, msg):
        console.print(f"[blue]{msg}[/blue]")

    def add_issue(
        self,
        label: str = "",
        description: str = "",
        cwe: str = "",
        affected_items: list[str] = (),
        references: list[str] = (),
    ) -> None:
        new_issue = Issue()
        new_issue.label = label
        new_issue.description = description
        new_issue.cwe = cwe
        new_issue.affected_items = affected_items
        new_issue.references = references
        self._issues.append(new_issue)

    def _print_module_label(self):
        self.info(f"[bold]====={self.title}=====[/bold]")
        console.print(f"[darkgray][italic]{self.description}[/italic][/darkgray]")

    def _print_results(self):
        if len(self._issues) == 0:
            self.success("No issues found!")
        else:
            for issue in self._issues:
                self.warning(issue.label)

    def check(self):
        raise NotImplementedError

    def run(self):
        self._print_module_label()
        self.check()
        self._print_results()
