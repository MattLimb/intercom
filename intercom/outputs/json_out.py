from intercom.outputs import BaseOutput
from ..exceptions import OutputConfigMissingKey, OutputConfigTypeError
import click
import json

__author__ = "Matt Limb <matt.limb17@gmail.com>"

class JSONOutput(BaseOutput):
    name = "json"

    def __init__(self, config, repo):
        self.config = config
        self.repo = repo
    
    def new(self, old, new, output_name):
        if str(self.repo) in self.config.get(f"outputs.{output_name}.software"):
            click.echo(json.dumps(
                dict(
                    repo=str(self.repo),
                    oldTag=old,
                    newTag=new,
                    message=f"New release for {str(self.repo)} - {new}",
                    output=output_name,
                ),
                indent=2
            ))
        
    def same(self, old, new):
        pass

    @staticmethod
    def verify_config(config):
        if "software" not in config.keys():
            raise OutputConfigMissingKey(f"'software' key missing from {JSONOutput.name} output config definition.")
        else:
            if type(config["software"]) != list:
                raise OutputConfigTypeError(f"'software' key wrong type in {JSONOutput.name} output config definition. - ")
        
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.config)}, {repr(self.repo)})"