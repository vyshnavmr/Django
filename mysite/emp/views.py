from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def employee_list(request):

    employees = [
        {"name": "Rahul Sharma", "job_title": "Software Developer", "salary": 60000, "is_full_time": True},
        {"name": "Priya Nair", "job_title": "UI Designer", "salary": 40000, "is_full_time": False},
        {"name": "Arjun Kumar", "job_title": "Project Manager", "salary": 75000, "is_full_time": True},
    ]

    return render(request, "emp.html", {"employees": employees})