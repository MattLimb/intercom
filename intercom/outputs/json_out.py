from intercom.outputs import BaseOutput
import click
import json

class JSONOutput(BaseOutput):
    name = "json"

    def __init__(self, config, repo):
        self.config = config
        self.repo = repo
    
    def run(self, old, new):
        
        click.echo(json.dumps(
            dict(
                repo=str(self.repo),
                oldTag=old,
                newTag=new,
                message=f"New tag for {str(self.repo)} - {new}"
            ),
            indent=2
        ))

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.config)}, {repr(self.repo)})"