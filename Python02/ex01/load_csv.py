"""_summary_
"""

import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """_summary_

    Args:
        path (str): _description_

    Returns:
        Dataset: _description_
    """
    try:
        if os.path.exists(path) is False:
            raise AssertionError("File does not exist.")
        if path.endswith('.csv') is False:
            raise AssertionError("Wrong file format")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimentions ({len(dataset.axes[0])}, {len(dataset.axes[1])})")
        return(dataset)
    except AssertionError as e:
        print(f"Error: {e}")
        return None