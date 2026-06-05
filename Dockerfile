FROM python:3.8-slim

# Set environment variables to prevent python from writing .pyc file & We need to ensure Python out is not buffered.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Installing System Environment (Requirement for Tensorflow)
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libhdfs-dev \
    protobuf-compiler \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setting the working directory
WORKDIR /app

# Copy the application code
COPY ..

# Installing dependencies from requirements.txt
RUN pip install --no-cache-dir -e .

# Train the model before running the application
RUN python pipeline/pipeline.py

# Espose the Port that Flask will run
EXPOSE 5000

# COMMAND to run the app
CMD ["python","application.py"]