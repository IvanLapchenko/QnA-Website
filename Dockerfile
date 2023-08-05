# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project files to the container
COPY . .

# Expose the port the Django application will run on
EXPOSE 8000

# Set the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
