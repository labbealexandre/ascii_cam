"""OpenCV capture methods."""

import screeninfo  #type: ignore
import cv2  # type: ignore

from src import types


def _get_frame_dimension(frame: types.Frame) -> int:
    """Extract the dimension of the frame."""

    n_dim = len(frame.shape)
    if n_dim not in [2, 3]:
        raise ValueError('The dimension of the frame should be 2 or 3')

    return n_dim


def get_frame_size(frame: types.Frame) -> types.FrameDimension:
    """Extract the width and the height of the frame."""

    _get_frame_dimension(frame)
    return {'height': frame.shape[0], 'width': frame.shape[1]}


def get_screen_size() -> types.FrameDimension:
    """Extract the width and the height of the screen."""

    screen = screeninfo.get_monitors()[0]
    return {'height': screen.height, 'width': screen.width}


def set_full_screen(frame_name: str) -> None:
    """Display full screen images."""

    cv2.namedWindow(frame_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(frame_name, cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
