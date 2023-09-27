from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.employees.models import leaveCategory, leaveApplication


class TestLeaveCategory(TestCase):
    def test_model_str(self):
        leave = leaveCategory.objects.create(leave="Sick Leave")
        self.assertEqual(str(leave), "Sick Leave")


class TestLeaveApplication(TestCase):
    def test_leave_start_validator(self):
        with self.assertRaises(ValidationError):
            leaveApplication.objects.create(leave_start="26/09/2023")

    def test_leave_end_validator(self):
        with self.assertRaises(ValidationError):
            leaveApplication.objects.create(leave_end="26/09/2023")
