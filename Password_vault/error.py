class Error(Exception):
    """Base class for other exception"""
    pass

class NoValueFound(Error):
    """Raised when no value is found"""
    pass