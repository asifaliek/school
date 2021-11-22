from django import forms
from django.forms.widgets import TextInput,Textarea,Select,EmailInput,FileInput
from .models import Student,Score,Subject


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('student_id',)
        widgets = {
            'name':TextInput(attrs = {'placeholder':'Name'}),
            'phone':TextInput(attrs = {'placeholder':'Phone'}),
            'email':EmailInput(attrs = {'placeholder':'E-mail'}),
            'address':Textarea(attrs = {'placeholder':'Address'}),
            'photo':FileInput(attrs = {'placeholder':'Photo'}),
            'branch':Select()
        }

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('__all__')
        widgets = {
            'student':Select(),
            'subject':Select(),
            'score':TextInput(attrs = {'placeholder':'Score'})
        }