"""Logger methods."""

from src import capture


def log_frame_info(frame) -> None:
    """Log the width and the height of the frame."""

    frame_dim = capture.get_frame_size(frame)
    rows, cols = frame_dim['height'], frame_dim['width']
    print(f'The size of the frame if {rows}x{cols}')
