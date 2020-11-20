from .base import BaseSource
from . import GitLabConfigMissingKey

import gitlab

class GitLabSource(BaseSource):
    def __init__(self, name, **kwargs):
        self.name = name
        self.project_id = kwargs.get("project_id")
        self.tag = kwargs.get("tag")

    @property
    def repo(self):
        repo_url = gitlab.Gitlab("https://gitlab.com/").projects.get(self.project_id).web_url
        repo_split = repo_url.split("/")
            
        return f"{repo_split[-2]}/{repo_split[-1]}"

    def get_latest(self):
        latest_tag = gitlab.Gitlab("https://gitlab.com/") \
            .projects.get(self.project_id).releases.list(sort="desc")[0].tag_name
    
        return latest_tag

    @staticmethod
    def verify_config(config):
        if "project_id" not in config.keys():
            raise GitLabConfigMissingKey("'project_id' not found in GitHub repo definintion")
            
        if "tag" not in config.keys():
            raise GitLabConfigMissingKey("'tag' not found in GitHub repo definintion")

        return True

    def __str__(self):
        return self.name
        
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, project_id={self.project_id!r}, tag={self.tag!r})" 