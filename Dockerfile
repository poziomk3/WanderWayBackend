# Dockerfile
# Use the official Python image as a base
FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of your Django application code
COPY . /app/

# Run migrations and start the Django development server
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec python manage.py runserver 0.0.0.0:8000"]