from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.

def main(request):
    pass


def login(request):
    return render(request, 'PostIt/login.html')


def signup(request: HttpRequest):
    if request.method == 'POST':
        id: str = request.POST.get('id', '')
        password: str = request.POST.get('pass', '')

        context = {}

        if User.objects.get(username=id) is not None:
            context["message"] = "Already exist account id"
            return render(request, 'PostIt/signup.html', context)

        if len(id) < 5:
            context["message"] = "Too short id"
            return render(request, 'PostIt/signup.html', context)

        if len(id) > 32:
            context["message"] = "Too long id"
            return render(request, 'PostIt/signup.html', context)

        if len(password) < 8:
            context["message"] = "Too short password"
            return render(request, 'PostIt/signup.html', context)

        if len(password) > 32:
            context["message"] = "Too long password"
            return render(request, 'PostIt/signup.html', context)

        user = User.objects.create_user(id, '', password)

        context["message"] = "Signup Complete"
        return render(request, 'PostIt/signup.html', context)
    else:
        return render(request, 'PostIt/signup.html')
