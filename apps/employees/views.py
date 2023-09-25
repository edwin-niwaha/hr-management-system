from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
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
    approved = (leaveApplication.objects.all().filter(leave_status="approved").count(),)
    rejected = (leaveApplication.objects.all().filter(leave_status="rejected").count(),)
    dict = {
        "request": requestLeave[0],
        "approved": approved[0],
        "rejected": rejected[0],
    }

    return render(request, "employees/user_dashboard.html", context=dict)


@login_required(login_url="/account/login-employee")
def addCategory(request):
    form = LeaveCategoryForm()

    if request.method == "POST":
        form = LeaveCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/employees/add-leave-category")

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
            return redirect("/employees/leave-request")
    return render(request, "employees/leave_request.html", context={"form": form})


@login_required(login_url="/account/login-employee")
def LeaveHistory(request):
    applications = leaveApplication.objects.filter(employee=request.user.employee)
    return render(
        request, "employees/leave_history.html", context={"applications": applications}
    )


@login_required(login_url="/account/login-employee")
def updateLeave(request, id, template_name="employees/leave_update.html"):
    leave = get_object_or_404(leaveApplication, id=id)
    form = LeaveRequestForm(request.POST or None, instance=leave)
    if form.is_valid():
        form.save()
        messages.success(request, "Application sent successfully!")
        return redirect("/employees/leave-history")
    return render(request, template_name, {"form": form})


@login_required(login_url="/account/login-employee")
def deleteLeave(request, id):
    loans = leaveApplication.objects.get(id=id)
    loans.delete()
    messages.success(request, "Deleted successfully!")
    return HttpResponseRedirect(reverse("emp:leave_history"))
