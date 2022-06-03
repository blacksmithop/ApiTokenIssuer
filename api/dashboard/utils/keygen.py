from secrets import token_urlsafe


def generate_key(len: int = 16) -> str:
    """A mock key generator using secrets module

    Args:
        len (int, optional): Length. Defaults to 16.

    Returns:
        str: Returns a key of length 16
    """
    return token_urlsafe(len)
