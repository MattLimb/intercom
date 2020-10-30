from .base import BaseSource
from . import GitHubConfigMissingKey

from github import Github

class GitHubSource(BaseSource):
    def __init__(self, name, **kwargs):
        self.name = name
        self.repo_url = kwargs.get("url")
        self.tag = kwargs.get("tag")

    @property
    def repo(self):
        slash_count = [ char for char in self.repo_url ].count("/")
        if slash_count == 1:
            return self.repo_url
        elif slash_count > 1:
            raw_split = self.repo_url.split("/")
            account = None
            repository = None

            if ( raw_split[0] == "http:" ) or ( raw_split[0] == "https:" ):
                account = raw_split[3]
                repository = raw_split[4]
            elif raw_split[0] == "github.com":
                account = raw_split[1]
                repository = raw_split[2]
            
            return f"{account}/{repository}"

    def get_latest(self):
        latest_tag = Github().get_repo(self.repo) \
            .get_latest_release().tag_name
    
        return latest_tag

    @staticmethod
    def verify_config(config):
        if "url" not in config.keys():
            raise GitHubConfigMissingKey("'url' not found in GitHub repo definintion")
            
        if "tag" not in config.keys():
            raise GitHubConfigMissingKey("'tag' not found in GitHub repo definintion")

        return True

    def __str__(self):
        return self.name
        
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, repo_url={self.repo_url!r}, tag={self.tag!r})" 