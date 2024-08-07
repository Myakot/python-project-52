# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app/

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "task_manager.wsgi:application"]