from django.shortcuts import render
from .forms import LoginForm

def login(request):

    print(request.method)
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            print(username)
            email = request.POST.get('email')
            password = request.POST.get('password')

            return render(request, 'output.html', {
                'username': username,
                'email': email,
                'password': password
            })
    else:
        form = LoginForm()

    return render(request, 'index.html', {'form': form})