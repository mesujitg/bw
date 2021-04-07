from django import forms
from courses.models import Course


class CourseForm(forms.ModelForm):
    # name = forms.TextInput()
    # duration = forms.TextInput()
    # details = forms.Textarea()
    # fee = forms.NumberInput()
    # image = forms.ImageField()

    class Meta:
        model = Course
        fields = "__all__"
        # fields = ['name', 'duration', 'details', 'fee', 'image']

