from django.shortcuts import render
from django.views.generic  import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
class JobDetails(TemplateView):
    template_name = 'job-detail.html'
class JobsView(TemplateView):
    template_name = 'jobs.html'
class UserProfileView(TemplateView):
    template_name  = 'user-profile.html'
class SearchView(TemplateView):
    template_name = 'search.html'
class AboutView(TemplateView):
    template_name = 'about.html'
class ContactView(TemplateView):
    template_name = 'contact.html'
class LoginView(TemplateView):
    template_name = 'signup.html'
