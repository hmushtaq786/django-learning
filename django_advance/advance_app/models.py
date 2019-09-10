from django.db import models
from django.urls import reverse
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=50)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('advance_app:detail', kwargs={'pk':self.pk})

class Student(models.Model):
    std_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(
        School, related_name='students', on_delete=models.CASCADE)  # related name connects this foreign key with school this way we can connect both tables

    def __str__(self):
        return self.std_name
