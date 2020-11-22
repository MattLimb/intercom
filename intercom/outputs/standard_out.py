from intercom.outputs import BaseOutput
from ..exceptions import OutputConfigMissingKey, OutputConfigTypeError
import click

__author__ = "Matt Limb <matt.limb17@gmail.com>"

class StandardOutput(BaseOutput):
    name = "stdout"

    def __init__(self, config, repo):
        self.config = config
        self.repo = repo
    
    def new(self, old, new, output_name):
        if str(self.repo) in self.config.get(f"outputs.{output_name}.software"):
            click.echo(f"New Tag for {str(self.repo)}: {new}")

    def same(self, old, new, output_name):
        if str(self.repo) in self.config.get(f"outputs.{output_name}.software"):
            click.echo(f"Current Tag for {str(self.repo)} ({new}) is the newest.")
    
    @staticmethod
    def override(repo_name, old, new, output_name):
        click.echo(f"New Tag for {str(repo_name)}: {new}")

    @staticmethod
    def verify_config(config):
        if "software" not in config.keys():
            raise OutputConfigMissingKey(f"'software' key missing from {StandardOutput.name} output config definition.")
        else:
            if type(config["software"]) != list:
                raise OutputConfigTypeError(f"'software' key wrong type in {StandardOutput.name} output config definition. - ")
        
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.config)}, {repr(self.repo)})"