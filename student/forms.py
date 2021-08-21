from django import forms
from django.db.models import fields
from .models import Marks, Question
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class Questionform(forms.ModelForm):
    class Meta:
        model=Question
        fields='__all__'

class Marksform(forms.ModelForm):
    class Meta:
        model=Marks
        fields='__all__'