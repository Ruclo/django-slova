from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username", "password1", "password2", 'groups')
#
#     # def save(self, commit=True):
#     #     user = super(CustomUserCreationForm, self).save(commit=False)
#     #     user.groups = self.cleaned_data["groups"]
#     #     if commit:
#     #         user.save()
#     #     return user