from .sources import GitHubSource, GitLabSource
from .exceptions import SourceNotSupported
import yaml
import pathlib

class IntercomConfig(object):
    _class_mappings = {
        "github": GitHubSource,
        "gitlab": GitLabSource
    }

    def __init__(self, config_location):
        self.config_location = pathlib.Path(str(config_location))
        self.configuration = None

        self._read_config()
        self.verify_config()

        self._iter_count = 0
        self._total_count = None

    def _read_config(self):
        with self.config_location.open("r") as f:
            self.configuration = yaml.safe_load(f.read())
    
    def verify_config(self):
        for key in self.get("software", default={}).keys():
            repo = self.get(f"software.{key}")
            if "service" in repo.keys():
                try:
                    self._class_mappings[repo.get("service")].verify_config(repo)
                    yield f"{key} Passed"
                except KeyError as e:
                    yield f"{key} Failed to Verify - {e}"

    def save(self):
        with self.config_location.open("w") as f:
            self.configuration = f.write(yaml.safe_dump(self.configuration, indent=2))
        
        self._read_config()

    def get(self, key_str, default=None, delimeter="."):
        config = self.configuration
        keys = key_str.split(delimeter)
        
        tmp_storage = config

        for key in keys:
            tmp_storage = tmp_storage.get(key, default)
            if tmp_storage == default:
                break

        return tmp_storage

    def update(self, key_str, value, delimeter=".", save=False):
        config = self.configuration
        keys = key_str.split(delimeter)
        
        for key in keys[:-1]:
            config = config[key]

        config[keys[-1]] = value

        if save:
            self.save()

    def __iter__(self):
        self._total_count = len(self.get("software"))
        self._software_keys = list(self.configuration.get("software").keys())
        return self

    def __next__(self):
        if self._iter_count >= self._total_count:
            raise StopIteration
        
        conf = self.get(f"software.{self._software_keys[self._iter_count]}")

        software = None

        if conf.get("service") not in self._class_mappings.keys():
            raise SourceNotSupported(f"Source {conf.get('service')} is currently not supported.")
            
        software = self._class_mappings[conf.get("service")](name=self._software_keys[self._iter_count], **conf)

        self._iter_count += 1
        return software