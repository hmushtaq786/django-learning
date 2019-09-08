from django.urls import path
from form_app import views

app_name = 'form_app'

urlpatterns = [
    path('', views.form_name_view, name='form_name'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('special/', views.special, name='special'),
]
