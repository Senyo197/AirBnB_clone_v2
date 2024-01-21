# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory to /app
WORKDIR /AirBnB_clone_v2

# Copy the current directory contents into the container at /app
COPY . /AirBnB_clone_v2

# Install any needed packages specified in requirements.txt
# RUN pip3 install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
# CMD ["python", "app.py"]

