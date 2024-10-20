from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # You can add other User fields if needed


class ProfileUpdateForm(forms.ModelForm):
    skills = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Add your skills separated by commas'}),
        required=False
    )

    class Meta:
        model = Profile
        fields = ['profile_image', 'bio', 'skills']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize skills as a comma-separated string or an empty string
        self.fields['skills'].initial = ', '.join(self.instance.skills) if self.instance.skills else ''

    def save(self, commit=True):
        # Convert skills string to a list and save the instance
        instance = super().save(commit=False)
        instance.skills = [skill.strip() for skill in self.cleaned_data['skills'].split(',') if skill.strip()]
        if commit:
            instance.save()
        return instance