def all_thing_is_obj(obj: any) -> int: # type: ignore
    if isinstance(obj, str):
        print(f"{obj} is in the kitchen : {type(obj)}")
    elif isinstance(obj, list) or isinstance(obj, tuple) or \
        isinstance(obj, dict) or isinstance(obj, set):
        print(f"{(type(obj).__name__).capitalize()} : {type(obj)}")
    else:
        print("Type not found")
    return 42
