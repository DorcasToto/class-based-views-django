from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.StudentList.as_view()),
    path('students/<pk>/',views.StudentDetail.as_view())

]