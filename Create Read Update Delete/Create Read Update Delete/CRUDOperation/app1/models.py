from django.db import models

class EmpModel(models.Model):
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    salary = models.IntegerField()
    isactive = models.BooleanField(default=True)

    # class Meta:
    #     db_table = "employee"

