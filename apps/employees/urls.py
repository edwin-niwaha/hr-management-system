from django.urls import path
from apps.employees import views


app_name = "employees"
urlpatterns = [
    path("user-dashboard/", views.UserDashboard, name="user_dashboard"),
    path("add-leave-category/", views.addCategory, name="add_category"),
    path("leave-request/", views.LeaveRequest, name="leave_request"),
    path(
        "leave-history/",
        views.LeaveHistory,
        name="leave_history",
    ),
    path("update-leave/<int:id>", views.updateLeave, name="update_leave"),
    path("delete-leave/<str:id>", views.deleteLeave, name="delete_leave"),
]
