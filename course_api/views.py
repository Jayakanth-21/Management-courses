from django.shortcuts import render
from rest_framework import generics
from .models import CourseMaster,Student,Enrollment
from .serializers import CourseMasterSerializer,StudentSerializer,EnrollmentSerializer

# Create your views here.


class CourseMasterApi(generics.ListAPIView):
    "list of avaialble courses"
    queryset = CourseMaster.objects.all()
    serializer_class = CourseMasterSerializer


class StudentCreateAPI(generics.CreateAPIView):
    """ Add a new student"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListAPI(generics.ListAPIView):
    """ list of all students """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EnrollmentAPI(generics.ListAPIView):
    """ all students who are currently enrolled"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class CourseEnrollAPI(generics.ListAPIView):
    """list of students enrolled in a particular course , """
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        course_pk = self.request.parser_context.get('kwargs')['course_pk']
        queryset = Enrollment.objects.filter(course_id=course_pk)
        return queryset


class CompletedCourseAPI(generics.ListAPIView):
    """list of students who have complete a course"""
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        return Enrollment.objects.filter(status=True)

