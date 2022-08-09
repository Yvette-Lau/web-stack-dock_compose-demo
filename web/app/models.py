from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        db_table="employee"
    def __str__(self):
        return '{} {} {}'.format(self.empid, self.empname, self.email)
