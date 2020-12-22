from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
from django.urls import reverse

from PostIt.models import PostIt


def main(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("login")

    user: User = request.user

    list = user.postit.all()

    context = {
        'post_list': list,
    }

    return render(request, 'PostIt/main.html', context)


def post(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method != 'POST':
        return redirect("./")

    content = request.POST.get('content', '')

    if content == "":
        return redirect("./")

    PostIt.objects.create(content=content, author=request.user)

    return redirect("./")

def logout(request):
    if not request.user.is_authenticated:
        return redirect("login")

    auth.logout(request)
    return redirect(f"{reverse('login')}?from=logout")


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("./")

    if request.method == 'POST':
        id: str = request.POST.get('id', '')
        password: str = request.POST.get('pass', '')
        user = auth.authenticate(request, username=id, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("./")

        context = {"message": "Invalid user or password"}
        return render(request, 'PostIt/login.html', context)

    if request.GET.get('from', '') == "logout":
        context = {"message": "Successfully logged out"}
        return render(request, 'PostIt/login.html', context)

    return render(request, 'PostIt/login.html')


def signup(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect("./")

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
