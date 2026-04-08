from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path('<str:msg>/', views.teacher_list, name='list'),
]