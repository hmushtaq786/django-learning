from django.shortcuts import render
from form_app import forms
from form_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'form_app/admin_forms/index.html')


def form_name_view(request):
    form = forms.InfoForm()

    if request.method == 'POST':
        form = forms.InfoForm(request.POST)

        if form.is_valid():
            print('Validation Success!')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'form_app/form_page.html', {'form': form})


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'form_app/admin_forms/registeration.html', {'registered': registered, 'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Automatically authenticate the user for you
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print('Someone tried to login and failed!')
            print('Username: {} and Password: {}'.format(username, password))
            return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, 'form_app/admin_forms/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# special view for logged in users
@login_required
def special(request):
    return render(request, 'form_app/admin_forms/special.html', {})
