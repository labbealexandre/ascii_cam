"""Engine that will run filter on the input."""

from typing import Any
from copy import deepcopy
import cv2  # type: ignore

from src import types
from src import capture as cp


# pylint: disable=too-many-branches
def run(cap: Any,
        frame_name: str,
        frame_filter: types.Filter,
        filter_kwargs: dict = None) -> None:
    """Display engine to run a specific filter."""

    if filter_kwargs is None:
        filter_kwargs = {}

    screen_size = cp.get_screen_size()

    while True:
        # Capture frame-by-frame
        frame = cap.read()[1]
        frame = cv2.flip(frame, 1)

        # Get the filtered output
        output_frame = frame_filter(frame, **filter_kwargs)

        # Display the resulting frame
        cv2.imshow(frame_name, output_frame)
        key_pressed = cv2.waitKey(1) & 0xFF

        # Stop the execution
        if key_pressed == ord('q'):
            raise RuntimeError(
                'The execution of the stream has been stopped by the user.')

        # Increase resolution
        if key_pressed == ord('l'):
            if 'output_size' not in filter_kwargs.keys():
                filter_kwargs['output_size'] = deepcopy(screen_size)
            else:
                filter_kwargs['output_size']['height'] = min(
                    screen_size['height'],
                    int(filter_kwargs['output_size']['height'] * 1.1))
                filter_kwargs['output_size']['width'] = min(
                    screen_size['width'],
                    int(filter_kwargs['output_size']['width'] * 1.1))

        # Decrease resolution
        if key_pressed == ord('j'):
            if 'output_size' not in filter_kwargs.keys():
                filter_kwargs['output_size'] = deepcopy(screen_size)
            else:
                filter_kwargs['output_size']['height'] = int(
                    filter_kwargs['output_size']['height'] / 1.1)
                filter_kwargs['output_size']['width'] = int(
                    filter_kwargs['output_size']['width'] / 1.1)

        # Zoom in
        if key_pressed == ord('i'):
            if 'zoom' not in filter_kwargs.keys():
                filter_kwargs['zoom'] = 1
            else:
                filter_kwargs['zoom'] *= 1.1

        # Zoom out
        if key_pressed == ord('k'):
            if 'zoom' not in filter_kwargs.keys():
                filter_kwargs['zoom'] = 1
            else:
                filter_kwargs['zoom'] = max(1, filter_kwargs['zoom'] / 1.1)

        # Take a picture
        if key_pressed == ord('p'):
            cp.save_picture(output_frame)
