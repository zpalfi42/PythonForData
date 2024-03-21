def square(x: int | float) -> int | float:
    """_summary_

    Args:
        x (int | float): _description_

    Returns:
        int | float: _description_
    """
    return x*x

def pow(x: int | float) -> int | float:
    """_summary_

    Args:
        x (int | float): _description_

    Returns:
        int | float: _description_
    """
    return x**x

def outer(x: int | float, function) -> object:
    """_summary_

    Args:
        x (int | float): _description_

    Returns:
        object: _description_
    """
    count = x
    def inner() -> float:
        """_summary_

        Returns:
            float: _description_
        """
        nonlocal count
        count = function(count)
        return count
    return inner