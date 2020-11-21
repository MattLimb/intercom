from intercom.outputs import BaseOutput
from ..exceptions import OutputConfigMissingKey, OutputConfigTypeError
import requests
import base64

__author__ = "Matt Limb <matt.limb17@gmail.com>"

class WebhookOutput(BaseOutput):
    name = "webhook"

    def __init__(self, config, repo):
        self.config = config
        self.repo = repo
    
    def _auth(self, output_name):
        webhook_type = self.config.get(f"outputs.{output_name}.auth", "none")
        if webhook_type == "basic":
            usr_pass = base64.b64encode(f"{self.config.get(f'outputs.{output_name}.username')}:{self.config.get(f'outputs.{output_name}.password')}".encode())
            header_text = f"Basic {usr_pass.decode()}"
        elif webhook_type == "bearer":
            header_text = f"Bearer {self.config.get(f'outputs.{output_name}.token')}"
        else:
            header_text = None
        
        return header_text

    def new(self, old, new, output_name):
        if str(self.repo) in self.config.get(f"outputs.{output_name}.software"):
            auth = self._auth(output_name)
            headers = {}

            if auth != None:
                headers["Authorization"] = auth

            url = self.config.get(f"outputs.{output_name}.url")
            
            data = dict(
                repo=str(self.repo),
                oldTag=old,
                newTag=new,
                message=f"New release for {str(self.repo)} - {new}",
                output=output_name
            )

            requests.get(url, json=data, headers=headers)
            
    def same(self, old, new):
        pass

    @staticmethod
    def verify_config(config):
        if "software" not in config.keys():
            raise OutputConfigMissingKey(f"'software' key missing from {WebhookOutput.name} output config definition.")
        else:
            if type(config["software"]) != list:
                raise OutputConfigTypeError(f"'software' key wrong type in {WebhookOutput.name} output config definition.")

        if "auth" not in config.keys():
            raise OutputConfigMissingKey(f"'auth' key missing from {WebhookOutput.name} output config definition.")
        else: 
            if config["auth"] == "basic":
                if "username" not in config.keys():
                    raise OutputConfigMissingKey(f"'username' key missing from {WebhookOutput.name} output config definition.")
                if "password" not in config.keys():
                    raise OutputConfigMissingKey(f"'password' key missing from {WebhookOutput.name} output config definition.")
            elif config["auth"] == "bearer":
                if "token" not in config.keys():
                    raise OutputConfigMissingKey(f"'token' key missing from {WebhookOutput.name} output config definition.")
        
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.config)}, {repr(self.repo)})"