pip
python -m venv venv
.\venv\Scripts\activate
pip install django
python -m django --version
django-admin startproject mysite djangotutorial
cd djangotutorial
python manage.py runserver
python manage.py migrate
python manage.py startapp polls
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
        python manage.py makemigrations polls
python manage.py migrate
python manage.py createsuperuser
from django.contrib import admin
from .models import Question

admin.site.register(Question)
__pycache__/
*.py[cod]
db.sqlite3
venv/
.venv/
git init
git add .
git commit -m "Completed Django tutorial: installation, models, admin"
