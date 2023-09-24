from django import forms
from .models import leaveApplication, leaveCategory


class LeaveCategoryForm(forms.ModelForm):
    class Meta:
        model = leaveCategory
        fields = "__all__"


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = leaveApplication
        fields = (
            "category",
            "leave_start",
            "leave_end",
        )
        widgets = {
            "remarks": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "leave_start": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd",
                    "class": "form-control",
                }
            ),
            "leave_end": forms.DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "yyyy-mm-dd",
                    "class": "form-control",
                }
            ),
        }
        labels = {
            "remarks": "Enter Remarks",
            "category": "Choose leave category",
            "leave_start": "Leave start date",
            "leave_end": "Leave end date",
        }
