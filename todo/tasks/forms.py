from django import forms


from .models import *
class TaskForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new Task'}))

    class Meta:
        model=Task
        fields = '__all__'