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
        fields = ['profile_image', 'bio', 'location', 'skills']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        skills = self.instance.skills
        if not skills or skills == []:
            self.fields['skills'].initial = ''  # If skills is empty, show empty string
        else:
            # Convert the list to a comma-separated string
            self.fields['skills'].initial = ', '.join(skills)

    def save(self, commit=True):
        # Override save method to convert skills back to a list
        instance = super(ProfileUpdateForm, self).save(commit=False)
        skills_string = self.cleaned_data.get('skills', '')
        instance.skills = [skill.strip() for skill in skills_string.split(',') if skill.strip()]
        if commit:
            instance.save()
        return instance