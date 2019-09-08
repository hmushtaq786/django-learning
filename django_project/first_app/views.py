from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

## IMPORTING THE MODELS
from first_app.models import Topic, Webpage, AccessRecord

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print('received')
            return HttpResponse('Received')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        
    return render(request, 'login.html', {'form': form})

def loggedin(request):
    return render(request, 'loggedin.html', {'username': NameForm().your_name})

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    return render(request, 'index.html', context=date_dict)