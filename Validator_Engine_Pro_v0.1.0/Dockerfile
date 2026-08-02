# Use an official, lightweight Python runtime as a parent image
FROM python:3.11-slim

# Set system environment variables to optimize Python performance
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the secure internal working directory inside the container
WORKDIR /app

# Copy the dependency matrix and local testing infrastructure
COPY test_load.py .

# Expose internal execution channels (Optional for async microservices)
EXPOSE 8080

# Command to automatically execute the local performance benchmark load test
CMD ["python", "test_load.py"]
