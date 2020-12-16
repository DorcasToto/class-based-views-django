from django.db import models

# Create your models here.
class Student(models.Model):
    registration_no = models.CharField(max_length=30)
    fullname = models.CharField(max_length=50)
    age = models.IntegerField(default = 0)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname