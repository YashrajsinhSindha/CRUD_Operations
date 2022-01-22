from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.TextField()
    department=models.TextField()

    def __str__(self):
        return str(self.name)+" "+str(self.email)

    class Meta:
        db_table='students'

