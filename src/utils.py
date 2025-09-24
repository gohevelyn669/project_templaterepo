# src/utils.py

import os
import random
import numpy as np

def set_seed(seed: int = 42):
    """
    Fix random seeds for reproducibility.
    Works for Python's random, NumPy, and hashing.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
