from django.db import models

class Course(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_n = models.CharField(max_length=50)
    last_n= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_n} {self.last_n}"


class Subject(models.Model):
    name = models.TextField()
    number = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.number}"