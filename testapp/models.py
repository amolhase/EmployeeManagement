from django.db import models



class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.CharField(max_length=20)
    econtact = models.CharField(max_length=30)
