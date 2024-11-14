import pytz
from django import forms
from .models import Task, StudentList


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']



class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

