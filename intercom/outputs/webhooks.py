from intercom.outputs import BaseOutput
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

    def new(self, old, new):
        for webhook in self.config.get("outputs", []):
            if str(self.repo) in self.config.get(f"outputs.{webhook}.software"):
                auth = self._auth(webhook)
                headers = {}

                if auth != None:
                    headers["Authorization"] = auth

                url = self.config.get(f"outputs.{webhook}.url")
                
                data = dict(
                    repo=str(self.repo),
                    oldTag=old,
                    newTag=new,
                    message=f"New release for {str(self.repo)} - {new}",
                    processWebhook=webhook
                )

                requests.get(url, json=data, headers=headers)
            
    def same(self, old, new):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.config)}, {repr(self.repo)})"