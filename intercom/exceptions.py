__author__ = "Matt Limb <matt.limb17@gmail.com>"

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
