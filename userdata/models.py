from django.db import models

class TrainingData(models.Model):
    item_name = models.CharField(max_length=200)
    item_status = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    vp = models.CharField(max_length=200)
    hire_date = models.DateTimeField('date_hired')