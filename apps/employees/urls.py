from django.urls import path
from apps.employees import views


app_name = "employees"
urlpatterns = [
    path("user-dashboard/", views.UserDashboard, name="user_dashboard"),
    path("add-leave-category/", views.add_category, name="add_category"),
    path("leave-request/", views.LeaveRequest, name="leave_request"),
    path(
        "employee-leave-history/",
        views.LeaveHistory,
        name="leave_history",
    ),
    path("update-leave/<int:id>", views.update_leave, name="update_leave"),
    # path("delete_leave/<str:id>", views.delete_loan, name="delete_loan"),
]
