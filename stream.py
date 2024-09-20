import os

# Set your YouTube stream key directly
YOUTUBE_STREAM_KEY = 'd9p4-k14d-b9c9-3fyr-f0xj'  # Replace with your actual stream key

# Check if the stream key is available
if not YOUTUBE_STREAM_KEY:
    print("Error: YouTube stream key is not set.")
    exit(1)

# Set the video file path
VIDEO_PATH = "cat.mp4"  # Ensure the file exists and has the correct path

# Set the FFmpeg command to stream the video on loop
ffmpeg_command = f"""
ffmpeg -re -stream_loop -1 -i {VIDEO_PATH} -vcodec libx264 -pix_fmt yuv420p -preset veryfast -maxrate 3000k -bufsize 6000k -acodec aac -ar 44100 -b:a 128k -f flv rtmp://a.rtmp.youtube.com/live2/{YOUTUBE_STREAM_KEY}
"""  # Make sure the triple quotes close here

# Run the FFmpeg command
os.system(ffmpeg_command)
