from django.shortcuts import render, redirect

students_data = [
    {"name": "Rahul"},
    {"name": "Anjali"},
    {"name": "Arun"},
]

def student_list(request, msg):

    if request.method == "POST":
        name = request.POST.get("name")
        students_data.append({"name": name})

        return redirect('students:list', msg="Student added successfully")

    context = {
        "students": students_data,
        "message": msg
    }

    return render(request, 'students/student_list.html', context)