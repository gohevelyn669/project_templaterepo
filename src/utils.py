# src/utils.py
import os
import random
import numpy as np

def set_seed(seed: int = 42):
    """
    Fix random seeds for reproducibility across common ML frameworks.
    Covers Python, NumPy, PyTorch, and TensorFlow (if installed).
    """
    os.environ["PYTHONHASHSEED"] = str(seed)

    # Python built-ins
    random.seed(seed)

    # NumPy
    np.random.seed(seed)

    # PyTorch
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)  # for multi-GPU
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        pass

    # TensorFlow
    try:
        import tensorflow as tf
        tf.random.set_seed(seed)
    except ImportError:
        pass
