from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import LeaveRequestForm, LeaveCategoryForm
from .models import leaveApplication


# Create your views here.


def home(request):
    return render(request, "home.html", context={})


@login_required(login_url="/account/login-employee")
def UserDashboard(request):
    requestLeave = (
        leaveApplication.objects.all().filter(employee=request.user.employee).count(),
    )
    dict = {
        "request": requestLeave[0],
    }

    return render(request, "employees/user_dashboard.html", context=dict)


@login_required(login_url="/account/login-employee")
def add_category(request):
    form = LeaveCategoryForm()

    if request.method == "POST":
        form = LeaveCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "employees/add_category.html", {"form": form})


@login_required(login_url="/account/login-employee")
def LeaveRequest(request):
    form = LeaveRequestForm()

    if request.method == "POST":
        form = LeaveRequestForm(request.POST)

        if form.is_valid():
            loan_obj = form.save(commit=False)
            loan_obj.employee = request.user.employee
            loan_obj.save()
            return redirect("/")

    return render(request, "employees/leave_request.html", context={"form": form})
