from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CourseMaster(models.Model):
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return self.course_name


class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    course = models.ForeignKey(CourseMaster,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)




