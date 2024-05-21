# students/urls.py
from django.urls import path
from .views import student_list, add_student, update_student, delete_student

urlpatterns = [
    path('', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    path('update/<int:pk>/', update_student, name='update_student'),
    path('delete/<int:pk>/', delete_student, name='delete_student'),
]
