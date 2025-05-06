# TunesToX

**TunesToX** is a simple desktop app that lets you combine an audio file and an optional image into a video with a watermark and quickly open the Twitter/X tweet composer to share your creation.

No Twitter API keys needed. No logins. No limits.

## Features

- Supports MP3, WAV, FLAC, M4A audio files
- Optional image support (JPG, PNG, etc.)
- If no image is provided, creates a black background video
- Adds a watermark automatically: `github.com/Gh0styTongue`
- Uses `ffmpeg` for fast video creation
- Opens the Twitter/X composer with your tweet text pre-filled
- Replaces the old video automatically if one exists

## Requirements

- Python 3.x
- `ffmpeg` installed and added to your system PATH
- `tkinter` (usually included with Python)

## Installation

1. Download the `Tunes.py` file.
2. Install `ffmpeg` and ensure it’s available from the command line (`ffmpeg --version` should work).

## Usage

1. Run the app:

    ```bash
    python Tunes.py
    ```

2. Select your audio file.
3. (Optional) Select an image.
4. Enter the tweet text you want to appear in the tweet.
5. Click **"Create Video & Open Twitter"**.
6. The video will be saved as `output_video.mp4`.
7. The tweet composer will open — upload the video and post!

## Example

No image:

- Creates a black 1280x720 video matching the length of your audio.
- Adds the watermark.

With image:

- Uses your image as the video background.
- Adds the watermark.

## Credits

Created by [Gh0styTongue](https://github.com/Gh0styTongue)

## License

MIT License
