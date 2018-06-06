from django import forms
from .models import App, AppDetail

class AppForm(forms.ModelForm):

    class Meta:
        model = App
        fields = ('app_name', 'team_name', 'status')



class AppDetailForm(forms.ModelForm):

    class Meta:
        model = AppDetail
        fields = ('team_manager_email', 'repo_link')
