from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class EmployeeSignUp(models.Model):
    user = models.OneToOneField(
        User, unique=True, on_delete=models.CASCADE, related_name="employee"
    )
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    address = models.CharField(
        max_length=250, default="Kampala, Uganda", blank=True, null=True
    )
    profile_picture = models.ImageField(
        upload_to="profile_pic",
    )
    designation = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "employee_signup"

    def __str__(self):
        return self.user.username
