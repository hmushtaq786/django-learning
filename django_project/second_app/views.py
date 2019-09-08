from django.shortcuts import render
from second_app.models import User
from second_app.forms import signup_form

# Create your views here.


def homepage(request):
    context_dict = {'heading': 'welcome to homepage!',
                    'ending': 'made with ❤️ by hamzakhan'}
    return render(request, 'homepage.html', context_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_list': user_list}

    return render(request, 'users.html', context=user_dict)


def signup(request):
    form = signup_form()
    if request.method == 'POST':
        form = signup_form(request.POST)

        if form.is_valid():
            form.save(commit=True)  # to commit it to the database
            return homepage(request)
        else:
            print('Error form invalid')
    return render(request, 'signup_form.html', context={'form': form})
