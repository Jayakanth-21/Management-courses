from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import CourseMasterApi,StudentCreateAPI,StudentListAPI,EnrollmentAPI,CourseEnrollAPI,CompletedCourseAPI


urlpatterns = [
    path('', TemplateView.as_view(template_name='course_api/index.html'), name='home_frontend'),
    path('courselist',CourseMasterApi.as_view()),

    path('studentadd',StudentCreateAPI.as_view()),
    path('studentlist',StudentListAPI.as_view()),

    path('enroll_list',EnrollmentAPI.as_view()),
    path('course_enroll/<int:course_pk>',CourseEnrollAPI.as_view()),
    path('completed',CompletedCourseAPI.as_view()),
]