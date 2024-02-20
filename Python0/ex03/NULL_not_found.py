from types import NoneType

prints_dict = {NoneType:"Nothing", int:"Zero", str:"Empty", bool:"Fake"}

def NULL_not_found(obj: any) -> int: # type: ignore
    if not obj:
        print(f"{prints_dict[type(obj)]}: {obj} {type(obj)}")
    elif obj != obj:
        print(f"Cheese: {obj} {type(obj)}")
    else:
        print("Type not Found")
    return 1
