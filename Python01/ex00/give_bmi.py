"""_summary_
"""


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """_summary_

    Args:
        height (list[int  |  float]): _description_
        weight (list[int  |  float]): _description_

    Returns:
        list[int | float]: _description_
    """
    try:
        if len(height) != len(weight)\
            and all(x > 0 and isinstance(x, (int, float)) for x in height)\
                is False\
                and all(x > 0 and isinstance(x, (int, float)) for x in weight)\
                is False:
            raise ValueError("Height and Weight lists have to be the same"
                             "lenght and must have only positive numbers")
        z = zip(height, weight)
        res = list((y/(x*x))for (x, y) in z)
        return res
    except ValueError as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """_summary_

    Args:
        bmi (list[int  |  float]): _description_
        limit (int): _description_

    Returns:
        list[bool]: _description_
    """
    try:
        if all(isinstance(x, (int, float)) for x in bmi) is False\
                and isinstance(limit, int) is False:
            raise ValueError("BMI list must contain only numbers and limit"
                             "should be a number")
        return list(x >= limit for x in bmi)
    except ValueError as e:
        print(f"Error: {e}")
        return []
