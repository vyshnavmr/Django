from django.shortcuts import render

def students(request):
    students = [
        {"name": "Arjun", "grade": 85, "passed": True},
        {"name": "Meera", "grade": 45, "passed": False},
        {"name": "Rahul", "grade": 72, "passed": True},
        {"name": "Anjali", "grade": 30, "passed": False},
    ]
    
    return render(request, 'students.html', {'students': students})