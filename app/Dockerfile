# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY app/app.py /app

# Install dependencies
RUN pip install --no-cache-dir flask

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Command to run the application
CMD ["python", "app.py"]