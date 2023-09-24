from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.login.models import EmployeeSignUp

# Create your models here.


class leaveCategory(models.Model):
    leave_name = models.CharField(max_length=100)
    leave_description = models.CharField(max_length=250)
    number_days_allowed = models.PositiveIntegerField(
        validators=[MaxValueValidator(30), MinValueValidator(0)]
    )
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.leave_name
        # return f"LeaveName: {self.leave_name}, Days: {self.number_days_allowed}"


class leaveApplication(models.Model):
    employee = models.ForeignKey(
        EmployeeSignUp, on_delete=models.CASCADE, related_name="employee_leave"
    )
    category = models.ForeignKey(leaveCategory, on_delete=models.CASCADE, null=True)
    date_of_application = models.DateField(auto_now_add=True)
    leave_start = models.DateField("start date")
    leave_end = models.DateField("end date")
    leave_status = models.CharField(max_length=50, default="pending")
    date_of_approval = models.DateField(auto_now_add=True)
    remarks = models.CharField(max_length=250)

    def __str__(self):
        return self.employee.user.username
