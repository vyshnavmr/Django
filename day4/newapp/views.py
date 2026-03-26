from django.shortcuts import render

def page(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        color = request.POST.get('color')
        return render(request,'result.html',{
         'formData':request.POST,
         'user': user
        }
    )
    return render(request,'page.html')

def form(request):
    if request.GET:
        user = request.GET.get('User')
        return render(request,'output.html',{
            'formData':request.GET,
        })
    return render(request,'form.html' )