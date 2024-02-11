from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class JobHolderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_id = models.CharField(max_length=20)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.user.username 
    

class JobRecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_website = models.URLField(max_length=200)

    def __str__(self):
        return self.user.username