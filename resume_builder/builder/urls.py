from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_resume, name='create_resume'),
    path('edit/<int:resume_id>/', views.edit_resume, name='edit_resume'),
    path('view/<int:resume_id>/', views.view_resume, name='view_resume'),
    path('delete/<int:resume_id>/', views.delete_resume, name='delete_resume'),
]
