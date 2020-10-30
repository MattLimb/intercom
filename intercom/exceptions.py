# Base Classes
class IntercomBase(Exception):
    pass

class IntercomSupportError(NotImplementedError):
    pass

class IntercomConfigKeyError(KeyError):
    pass



# "Real" Classes - Ones that are actually used.

class SourceNotSupported(IntercomSupportError):
    pass

class GitHubConfigMissingKey(IntercomConfigKeyError):
    pass
