from django.db import models

# Create your models here.
class department(models.Model):
    depName=models.CharField(max_length=50)
    d_slug=models.SlugField(max_length=50)
    def __str__(self):
        return '{}'.format(self.depName)

class courses(models.Model):
    depF=models.ForeignKey(department,on_delete=models.CASCADE)
    courseName=models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.courseName)

