from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    # path("", views.HomePageView.as_view(), name="home"),
    path("", views.index, name="feed_or_login"),
]