from django import forms
from django.contrib.auth.models import User
from .models import Profile, ProjectPost

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
        fields = ['profile_image', 'bio', 'skills']  # Leave out 'location'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize skills as a comma-separated string or an empty string
        self.fields['skills'].initial = ', '.join(self.instance.skills) if self.instance.skills else ''

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Convert skills string to a list and save the instance
        instance.skills = [skill.strip() for skill in self.cleaned_data['skills'].split(',') if skill.strip()]
        if commit:
            instance.save()
        return instance
    
class ProjectPostForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Add items separated by commas'}),
        required=False
    )
    skills = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Add skills separated by commas'}),
        required=False
    )
    categories = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Add categories separated by commas'}),
        required=False
    )



class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = ProjectPost
        fields = ['title', 'description', 'description_long', 'skills', 'categories', 'date']

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # If skills is already a list, don't split it
        if isinstance(self.cleaned_data['skills'], str):
            instance.skills = [skill.strip() for skill in self.cleaned_data['skills'].split(',') if skill.strip()]
        else:
            instance.skills = self.cleaned_data['skills']  # Already a list, no need to process

        # Do the same for categories if necessary
        if isinstance(self.cleaned_data['categories'], str):
            instance.categories = [category.strip() for category in self.cleaned_data['categories'].split(',') if category.strip()]
        else:
            instance.categories = self.cleaned_data['categories']

        if commit:
            instance.save()
        return instance