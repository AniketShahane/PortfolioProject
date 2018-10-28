from django.db import models

class Job(models.Model):
    #we want to have the jobs to have an image and small summary of 200 words
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
