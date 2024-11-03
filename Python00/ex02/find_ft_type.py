"""_summary_
"""


def all_thing_is_obj(obj: any) -> int:  # type: ignore
    """
    Checks the type of the given object and prints a message based on the type.

    Args:
        obj (any): The object whose type is to be checked. Can be a string, list, tuple, dict, set, or any other type.

    Returns:
        int: Always returns the integer 42.
    """
    if isinstance(obj, str):
        print(f"{obj} is in the kitchen : {type(obj)}")
    elif isinstance(obj, (list, tuple, dict, set)):
        print(f"{(type(obj).__name__).capitalize()} : {type(obj)}")
    else:
        print("Type not found")
    return 42
