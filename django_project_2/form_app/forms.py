from django import forms
from django.core import validators
from django.contrib.auth.models import User
from form_app.models import UserProfileInfo

# ##Custom validator
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name needs to start with z')


class InfoForm(forms.Form):
    name = forms.CharField()  #validators=[check_for_z]
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    ## To create a text area
    text = forms.CharField(widget=forms.Textarea)

    #clean method to validate whole form at once
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError('Make sure emails match!')

    # ## Form validation for bots
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) ## BUILT IN VALIDATION

    # ## another way of validating
    # # built in method with keyword 'clean_nameoftheelementwewanttovalidate'
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     # bots look at html so if our hidden field is filled in with some data it means it was a bot
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return botcatcher


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
