from django.views.generic import TemplateView
from django.shortcuts import redirect

def index(request):
    if(request.user.is_authenticated):
        return redirect("/feed/")
    else:
        return redirect("/accounts/login/")

class HomePageView(TemplateView):
    template_name = "home.html"