from django.urls import path
from django.urls import include
from second_app import views

app_name = 'second_app'

urlpatterns = [
    path('', views.users, name='users'),
    path('signup/', views.signup, name='signup')
    # path('logged-in', views.loggedin, name = 'loggedin')
]
