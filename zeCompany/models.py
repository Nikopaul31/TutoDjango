from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255, default='')
    age = models.IntegerField(default=0)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name