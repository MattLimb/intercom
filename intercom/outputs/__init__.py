from ._base import BaseOutput
from .standard_out import StandardOutput
from .json_out import JSONOutput

all_outputs = {
    StandardOutput.name: StandardOutput,
    JSONOutput.name: JSONOutput,
}