from rest_framework.serializers import ModelSerializer

from .models import CourseMaster,Student,Enrollment


class CourseMasterSerializer(ModelSerializer):
    class Meta:
        model = CourseMaster
        fields = ['pk','course_name']


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['pk','name']


class EnrollmentSerializer(ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseMasterSerializer(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['student','course']


