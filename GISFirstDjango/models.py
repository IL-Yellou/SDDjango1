from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    active_acc = models.BooleanField()

class TeachingGroup(models.Model):
    students = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)