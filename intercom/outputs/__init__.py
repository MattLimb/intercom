from ._base import BaseOutput
from .standard_out import StandardOutput
from .json_out import JSONOutput
from .webhooks import WebhookOutput

__author__ = "Matt Limb <matt.limb17@gmail.com>"

all_outputs = {
    StandardOutput.name: StandardOutput,
    JSONOutput.name: JSONOutput,
    WebhookOutput.name: WebhookOutput,
}

all_overrides = {
    StandardOutput.name: StandardOutput,
    JSONOutput.name: JSONOutput,
}