import os
from flask import Flask

app = Flask(__name__)

YOUTUBE_STREAM_KEY = 'd9p4-k14d-b9c9-3fyr-f0xj' 

if not YOUTUBE_STREAM_KEY:
    print("Error: YouTube stream key is not set.")
    exit(1)

VIDEO_PATH = "fblite_video-5.mp4" 
ffmpeg_command = f"""
ffmpeg -re -stream_loop -1 -i {VIDEO_PATH} -vcodec libx264 -pix_fmt yuv420p -preset veryfast -maxrate 3000k -bufsize 6000k -acodec aac -ar 44100 -b:a 128k -f flv rtmp://a.rtmp.youtube.com/live2/{YOUTUBE_STREAM_KEY}
"""  
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for Render"""
    return "OK", 200

if __name__ == '__main__':
    os.system(ffmpeg_command)
    
    # Start the Flask app on port 10000
    app.run(host='0.0.0.0', port=10000)
