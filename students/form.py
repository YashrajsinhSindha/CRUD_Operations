from django import forms
#import model class from models.py
#from app_name.models import model_name
from students.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
