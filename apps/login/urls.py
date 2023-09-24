from django.urls import path
from apps.login import views


app_name = "login"
urlpatterns = [
    path("login-employee/", views.login_view, name="login_employee"),
    path("signup-employee/", views.sign_up_view, name="signup_employee"),
    path("logout-employee/", views.logout_view, name="logout"),
    path("edit-employee/", views.edit_employee, name="edit-employee"),
]
