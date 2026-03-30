from django.shortcuts import render
from .forms import LoginForm
# Create your views here.

def home(request):

    print(request.method)
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            email = request.POST.get('email')
            password = request.POST.get('password')

            return render(request, 'output.html', {
                'email': email,
                'password': password
            })
    else:
        form = LoginForm()

    return render(request, 'home.html', {'form': form})