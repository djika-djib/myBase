from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_Name = models.CharField(max_length=100)
    Employee_Role = models.CharField(max_length=100)
    date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.Employee_Name

# Models for WebPAge

# class Topic(models.Model):
#     top_name = models.CharField(max_length=264, unique=True)

#     def __str__(self):
#         return self.top_name

class Webpage(models.Model):
    # topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.CharField(max_length=264)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

