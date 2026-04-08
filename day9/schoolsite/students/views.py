from django.shortcuts import render

# Hardcoded student data
students_data = [
    {"name": "Rahul", "marks": 85},
    {"name": "Anjali", "marks": 92},
    {"name": "Arun", "marks": 78},
]

# homepage
def home(request):
    return render(request, "home.html", {"students": students_data})

# result page
def result(request, name):
    student_result = None

    for student in students_data:
        if student["name"] == name:
            student_result = student

    return render(request, "result.html", {"student": student_result})