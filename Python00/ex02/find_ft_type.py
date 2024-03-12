"""_summary_
"""


def all_thing_is_obj(obj: any) -> int:  # type: ignore
    """_summary_

    Args:
        obj (any): _description_

    Returns:
        int: _description_
    """
    if isinstance(obj, str):
        print(f"{obj} is in the kitchen : {type(obj)}")
    elif isinstance(obj, (list, tuple, dict, set)):
        print(f"{(type(obj).__name__).capitalize()} : {type(obj)}")
    else:
        print("Type not found")
    return 42
