class FortniteApiException(Exception):
    pass


class FalseResult(FortniteApiException):
    """Raise when no api-key is provided"""
    pass
