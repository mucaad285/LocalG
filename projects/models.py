from django.db import models
from django import forms
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    objectives = models.TextField()
    outcome_perc = models.IntegerField()
    estimated_budget = models.IntegerField()
    actual_budget = models.IntegerField()
    started_date = models.DateField(null=True)
    finished_date = models.DateField(null=True)
    top_proj = models.BooleanField(default=False)
    mande_report = models.FileField(upload_to='Reports/',null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class ProjectGallery(models.Model):
    project = models.ForeignKey(Project,default=None , on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.project.title


class Comment(models.Model):
    project = models.ForeignKey(Project,default=None , on_delete=models.CASCADE)
    comment_txt = models.TextField()
    date_time = models.DateTimeField(auto_now_add=timezone.now)
    email = models.EmailField(default=None)
    name = models.CharField(max_length=100 , default=None)

    def __str__(self):
        return self.project.title

