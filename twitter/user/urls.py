from django.urls import path

from . import views

app_name = "tweet"

urlpatterns = [
    path('login', views.login, name="signin"),
    path('validate_login', views.validate_login, name="validate_login"),
    path('register', views.register, name="sinup"),
    path('validate_register', views.validate_register, name="validate_register"),
]
