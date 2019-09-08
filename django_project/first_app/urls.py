from django.urls import path
from django.urls import include
from first_app import views
urlpatterns = [
    path('', views.get_name, name='get_name'),
    path('index/', views.index, name='index'),
    # path('logged-in', views.loggedin, name = 'loggedin')
]
