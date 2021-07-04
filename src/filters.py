"""Filter methods."""

import cv2  # type: ignore
import numpy as np

from src import capture as cp
from src import types

ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', 'o', '%', '#']
ASCII_COLOR = (1, 1, 1)
ASCII_THICKNESS = 1
ASCII_FONT = cv2.FONT_HERSHEY_PLAIN


def grey_filter(frame: types.Frame) -> types.Frame:
    """Return a gray scale frame."""

    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def reduction_filter(frame: types.Frame) -> types.Frame:
    """Return a reduced gray scale frame."""
    def my_round(pixel):
        new_pixel = np.round(pixel / 32) * 32
        return new_pixel.astype(np.uint8)

    output = grey_filter(frame)
    output = my_round(output)

    return output


def zoom_filter(frame: types.Frame, zoom: float = 1) -> types.Frame:
    """Return a zoomed frame."""

    new_height, new_width = int(frame.shape[0] / zoom), int(frame.shape[1] /
                                                            zoom)
    top_offset, left_offset = (frame.shape[0] - new_height) // 2, (
        frame.shape[1] - new_width) // 2

    output = frame[top_offset:new_height + top_offset,
                   left_offset:new_width + left_offset]
    return output


def ascii_filter(frame: types.Frame,
                 output_size: types.FrameDimension = None,
                 zoom: float = 1,
                 is_grey: bool = False,
                 q: float = 1) -> types.Frame:
    """Return a frame filled with ascii letters."""

    if output_size is None:
        output_size = cp.get_screen_size()

    char_n = len(ASCII_CHARS)

    pixel_range = 256 / char_n

    # Initialize the output
    output = np.zeros((output_size['height'], output_size['width'], 3))

    # Crop the frame to have a zoom effect
    working_frame = zoom_filter(frame, zoom=zoom)

    # Convert the frame to gray scale
    working_frame = working_frame if is_grey else grey_filter(working_frame)

    # Resize the initial frame
    resized_rows, resized_cols = output_size['height'] // char_n, output_size[
        'width'] // char_n
    working_frame = cv2.resize(working_frame, (resized_cols, resized_rows),
                               interpolation=cv2.INTER_LINEAR)

    # Reduce the range of possible values to char_n
    def round_pixel(pixel):
        new_pixel = np.floor((pixel / pixel_range) / q)
        return new_pixel.astype(np.uint8)

    working_frame = round_pixel(working_frame)

    # Replace grey pixel to the corresponding letter
    for i in range(resized_rows):
        for j in range(resized_cols):
            output = cv2.putText(output, ASCII_CHARS[working_frame[i, j]],
                                 (j * char_n, (i + 1) * char_n - 1),
                                 ASCII_FONT, 1, ASCII_COLOR, ASCII_THICKNESS,
                                 cv2.LINE_AA)
    return output


def edges_filter(frame: types.Frame) -> types.Frame:
    """Return a frame with the edges of the input."""

    gray = grey_filter(frame)
    gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)
    output = cv2.Canny(gray_filtered, 20, 30)

    return output


def ascii_edges_filter(frame: types.Frame) -> types.Frame:
    """Return a frame with the ascii edges of the input."""

    edges = edges_filter(frame)
    output = ascii_filter(edges, is_grey=True)

    return output
