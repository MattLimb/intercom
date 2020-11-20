from intercom.outputs import BaseOutput
import click

__author__ = "Matt Limb <matt.limb17@gmail.com>"

class StandardOutput(BaseOutput):
    name = "stdout"

    def __init__(self, config, repo):
        self.config = config
        self.repo = repo
    
    def new(self, old, new):
        click.echo(f"New Tag for {str(self.repo)}: {new}")

    def same(self, old, new):
        click.echo(f"Current Tag for {str(self.repo)} ({new}) is the newest.")

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.config)}, {repr(self.repo)})"