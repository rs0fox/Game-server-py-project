# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install any system dependencies if needed
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    # Install any additional system dependencies here (e.g., build-essential, libffi-dev)
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run game.py when the container launches
CMD ["python", "game/game.py"]
