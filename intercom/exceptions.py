# Base Classes
class IntercomBase(Exception):
    pass

class IntercomSupportError(NotImplementedError):
    pass

class IntercomConfigKeyError(KeyError):
    pass

# Used Exceptions

class SourceNotSupported(IntercomSupportError):
    pass

class GitHubConfigMissingKey(IntercomConfigKeyError):
    pass

class GitLabConfigMissingKey(IntercomConfigKeyError):
    pass
