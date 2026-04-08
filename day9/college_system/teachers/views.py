from django.shortcuts import render, redirect

teachers_data = [
    {"name": "Joseph"},
    {"name": "Meera"},
    {"name": "David"},
]

def teacher_list(request, msg):

    if request.method == "POST":
        name = request.POST.get("name")
        teachers_data.append({"name": name})

        return redirect('teachers:list', msg="Teacher added successfully")

    context = {
        "teachers": teachers_data,
        "message": msg
    }

    return render(request, 'teachers/teacher_list.html', context)