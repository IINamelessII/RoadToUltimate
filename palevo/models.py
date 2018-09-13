from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=64)
    descr = models.CharField(max_length=500)
    #foto
    #rate

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Semester(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return str(self.number) + " semester"


class Subject(models.Model):
    name = models.CharField(max_length=32)
    descr = models.CharField(max_length=500)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    #materials

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=32)
    descr = models.CharField(max_length=500)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    #foto

    def __str__(self):
        return self.name


class Solution(models.Model):
    name = models.CharField(max_length=32)
    descr = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    #rate
    #files

    def __str__(self):
        return self.name
