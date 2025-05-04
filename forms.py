from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class BasicSignUpForm(UserCreationForm):
    location = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'location', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, location=self.cleaned_data['location'])
        return user
