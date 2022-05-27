from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    roll = models.PositiveIntegerField(null=True)
    course = models.CharField(max_length=150, null=True)
    stream = models.CharField( max_length=50, null=True)
    gender = models.CharField( max_length=30, null=True)
    year = models.PositiveSmallIntegerField(null=True)


    def __str__(self):
        return  '%s %s %d %s %s %s %d'%(self.name, self.email, self.roll, self.course, self.stream, self.gender, self.year)
