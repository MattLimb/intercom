from intercom.outputs import BaseOutput
import click

class StandardOutput(BaseOutput):
    name = "stdout"

    def __init__(self, config, repo):
        self.config = config
        self.repo = repo
    
    def run(self, old, new):
        click.echo(f"New Tag for {str(self.repo)}: {new}")

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.config)}, {repr(self.repo)})"