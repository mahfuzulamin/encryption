
def is_empty(value: str):
    """Checks if a string is null or empty.

    Parameters
    ----------
    value : str
        Input string  
    """
    if not value or len(value.strip()) == 0:
        return True
   
    return False