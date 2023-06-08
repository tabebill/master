# Use the Python Slim Buster base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the Flask application code to the working directory
COPY . .

# Expose port 5001 (assuming your Flask application runs on this port)
EXPOSE 5001

# Set the environment variables for AWS credentials
ENV AWS_ACCESS_KEY_ID=<your-access-key>
ENV AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
ENV AWS_DEFAULT_REGION=us-east-1

# Run the Flask application when the container starts
CMD ["python3", "app.py"]
