from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('lectures/<int:pk>/', views.lecture_detail, name='lecture_detail'),
    path('assignments/<int:pk>/', views.assignment_detail, name='assignment_detail'),
    path('submissions/<int:submission_id>/grade/', views.grade_submission, name='grade_submission'),
    path('login/', views.user_login, name='user_login'),
]