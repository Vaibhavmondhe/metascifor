from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('update-fee/<int:student_id>/', views.update_fee_status, name='update_fee_status'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
