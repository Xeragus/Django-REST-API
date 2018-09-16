from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname
