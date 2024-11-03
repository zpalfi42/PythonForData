"""_summary_
"""

import os

def ft_tqdm(lst: range) -> None:  # type: ignore
    """_summary_

    Args:
        lst (range): _description_
    """
    totalElems = len(lst)
    size = os.get_terminal_size()
    requiredCharacters = 8 + (len(str(totalElems)) * 2) + 27
    BAR_LEN = size.columns - requiredCharacters
    total = len(lst)
    for x, y in enumerate(lst):
        print(f"\r{' '*(1-int((x+1)/total))}{((x+1)/total)*100:.0f}%|█"
            f"{int(((x+1)/total)*BAR_LEN)*'█'}{(BAR_LEN-int(((x+1)/total)*BAR_LEN))*' '}"
            f"| {(x+1)}/{total}", end=" ", sep="")
        yield y  # type: ignore
