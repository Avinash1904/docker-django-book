# docker-django-book
Sample book app implementation with docker and django

This app is created for learning purpose on how we can implement django production ready, using docker

1. django-admin startproject bookstore_project .
   --> Adding . will remove creating bookstore_project folder twice

2. Create Dockerfile and docker-compose.yml to start the project, every configuration needs to be there itself.



**Templates**

We’ll also update TEMPLATES so that Django will look for a project-level templates folder. By default Django looks within each app for a templates folder, but organizing all templates in one space is easier to manage.
