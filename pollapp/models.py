from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class usermodel(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user = models.IntegerField(unique=True,auto_created=True,default=1)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.username.username
class poll_question(models.Model):
    id_poll = models.UUIDField(primary_key=True,default=uuid.uuid4())
    user = models.CharField(max_length=100,default='pbgp')
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
class poll_answer(models.Model):
    user = models.CharField(max_length=100,default='pbgp')
    id_answer = models.CharField(max_length=1000)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=500)
