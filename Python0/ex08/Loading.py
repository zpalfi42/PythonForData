"""_summary_
"""


def ft_tqdm(lst: range) -> None:  # type: ignore
    """_summary_

    Args:
        lst (range): _description_
    """
    total = len(lst)
    for x, y in enumerate(lst):
        print(f"\r{' '*(1-int((x+1)/total))}{((x+1)/total)*100:.0f}%|█"
              f"{int(((x+1)/total)*39)*'█'}{(39-int(((x+1)/total)*39))*' '}"
              f"| {(x+1)}/{total}", end=" ", sep="")
        yield y  # type: ignore
