import uuid
import datetime
from django.core.exceptions import ValidationError
from django.db import models
from apps.login.models import EmployeeSignUp

# Create your models here.


class leaveCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    leave = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "leave_categories"

    def __str__(self):
        return self.leave


class leaveApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(
        EmployeeSignUp, on_delete=models.CASCADE, related_name="employee_leave"
    )
    category = models.ForeignKey(leaveCategory, on_delete=models.CASCADE, null=True)
    date_of_application = models.DateField(auto_now_add=True)

    def Date_validation(value):
        if value < datetime.date.today():
            raise ValidationError("The date cannot be in the past")

    leave_start = models.DateField(
        default=datetime.date.today, validators=[Date_validation]
    )
    leave_end = models.DateField(
        default=datetime.date.today, validators=[Date_validation]
    )

    leave_status = models.CharField(max_length=50, default="pending")
    date_of_approval = models.DateField(auto_now_add=True)
    remarks = models.CharField(max_length=250)

    class Meta:
        db_table = "leave_applications"

    def __str__(self):
        return self.employee.user.username
