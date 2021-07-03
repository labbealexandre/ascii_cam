"""Engine that will run filter on the input."""

from typing import Any
import cv2  # type: ignore

from src import types
from src import capture as cp


def run(cap: Any,
        frame_name: str,
        frame_filter: types.Filter,
        filter_kwargs: dict = None) -> None:
    """Display engine to run a specific filter."""

    if filter_kwargs is None:
        filter_kwargs = {}

    while True:
        # Capture frame-by-frame
        frame = cap.read()[1]
        frame = cv2.flip(frame, 1)

        # Get the filtered output
        output_frame = frame_filter(frame, **filter_kwargs)

        # Display the resulting frame
        cv2.imshow(frame_name, output_frame)
        key_pressed = cv2.waitKey(1) & 0xFF
        if key_pressed == ord('q'):
            raise RuntimeError(
                'The execution of the stream has been stopped by the user.')
        if key_pressed == ord('p'):
            cp.save_picture(output_frame)
