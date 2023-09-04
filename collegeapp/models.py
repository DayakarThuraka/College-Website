from django.db import models

class  Branches(models.Model):
    branch_name=models.CharField(max_length=100)
    fee=models.IntegerField()
    duration=models.CharField(max_length=100)
    start_year=models.DateTimeField(max_length=100)
    passedout_year=models.DateTimeField(max_length=100)
    typeof_college=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class FeedBack(models.Model):
    comment=models.TextField(max_length=100)
    date=models.DateTimeField()

class FeedBackPage(models.Model):
    comment=models.TextField(max_length=100)
    username=models.CharField(max_length=100)
    date=models.DateTimeField()