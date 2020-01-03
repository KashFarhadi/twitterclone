## Welcome to Django! TwitterClone
Make Tweets and follow your friends just like in twitter but without all the bloatware and with cooler people.

### Completed by
Kash Farhadi

## Running the Application

Fork, Clone, Navigate to directory
Create and start a a virtual environment

for pipenv:
`pipenv -install`
`pipenv shell`

`python manage.py makemigrations {foldername}` 
(where foldername is the top level folder for this project)

`python manage.py migrate`

Create an admin account (superuser) if you would like to test admin features and access the admin page. Easily create users and objects from the built in django visual interface

`python manage.py createsuperuser`

Finally start the django server using: 
`python manage.py runserver`

Access the homepage at 
`http://127.0.0.1:8000/` 
`http://localhost:8000/`

Admin page
`http://127.0.0.1:8000/admin` 
`http://localhost:8000/admin`


##### Built using Python 3.8 and the latest version of Django (2.1.2 as of this writing)
