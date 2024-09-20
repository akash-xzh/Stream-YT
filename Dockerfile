# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y ffmpeg && pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run stream_to_youtube.py when the container launches
CMD ["python", "stream_to_youtube.py"]
