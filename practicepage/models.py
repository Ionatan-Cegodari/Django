from django.db import models

class People(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.IntegerField()

    def __str__(self):
        return f'{self.name} Birth Year {self.DOB}' #this makes the backend database look nice and all of that 