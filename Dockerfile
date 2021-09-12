# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code/

# Install Dependencies
RUN pip install django
RUN pip install psycopg2

# Copy project
COPY . /code/
