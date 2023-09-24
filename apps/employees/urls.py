from django.urls import path
from apps.employees import views


app_name = "employees"
urlpatterns = [
    path("add-leave-category/", views.add_category, name="add_category"),
    path("leave-request/", views.LeaveRequest, name="leave_request"),
    # path(
    #     "leave-history/",
    #     views.LeaveHistory,
    #     name="leave_history",
    # ),
    path("user-dashboard/", views.UserDashboard, name="user_dashboard"),
]
