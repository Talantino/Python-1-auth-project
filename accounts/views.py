from django.shortcuts import render, redirect

from .forms import CreateUserForm


def home_view(request):

    return render(request, "accounts/index.html")


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    context = {"registerform": form}
    return render(request, "accounts/register.html", context=context)


def login(request):

    return render(request, "accounts/login.html")


def dashboard(request):

    return render(request, "accounts/dashboard.html")


def logout(request):

    return render(request, "accounts/logout.html")
