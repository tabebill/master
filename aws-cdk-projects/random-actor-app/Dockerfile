# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the container
COPY app.py .
COPY templates/ templates/

# Expose port 5000 for Flask app
EXPOSE 5002

# Run the Flask app when the container starts
CMD ["python3", "app.py"]
