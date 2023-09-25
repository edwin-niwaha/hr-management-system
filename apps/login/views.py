from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import EmployeeSignUpForm, EmployeeLoginForm, UpdateEmployeeForm
from django.shortcuts import redirect
from .models import EmployeeSignUp
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def sign_up_view(request):
    error = ""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    form = EmployeeSignUpForm()
    if request.method == "POST":
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            user_profile = EmployeeSignUp(user=user)
            user_profile.save()
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            print(username, password1)
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))

            return HttpResponseRedirect(reverse("login:login_employee"))

        else:
            if User.objects.filter(username=request.POST["username"]).exists():
                error = "employee already exists"

            else:
                error = (
                    "Your password is not strong enough or both password must be same"
                )

    return render(
        request,
        "login/signup.html",
        context={"form": form, "user": "EMPLOYEE REGISTER", "error": error},
    )


def login_view(request):
    form = EmployeeLoginForm()
    if request.method == "POST":
        form = EmployeeLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))

        else:
            return render(
                request,
                "login/login.html",
                context={
                    "form": form,
                    "user": "EMPLOYEE LOGIN",
                    "error": "Invalid username or password",
                },
            )
    return render(
        request,
        "login/login.html",
        context={"form": form, "user": "EMPLOYEE LOGIN"},
    )


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


@login_required(login_url="/account/login-employee")
def edit_employee(request):
    employee = EmployeeSignUp.objects.get(user=request.user)
    form = UpdateEmployeeForm(instance=employee)
    if request.method == "POST":
        form = UpdateEmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid:
            employee = form.save(commit=False)
            employee.save()
            return HttpResponseRedirect(reverse("home"))
    return render(request, "login/edit.html", context={"form": form})
