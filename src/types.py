"""Custom types."""

from typing import Callable, TypedDict
import numpy as np


class FrameDimension(TypedDict):
    """Height and Width of a 2-Dimension Frame."""

    height: int
    width: int


Frame = np.ndarray
Filter = Callable  # FIXME: add the info that the first arg is np.ndarray
