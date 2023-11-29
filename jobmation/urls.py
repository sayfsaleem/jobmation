"""jobmation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(), name='home'),
    path('jobs/',views.JobsView.as_view(), name='job'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('search/',views.SearchView.as_view(), name='search'),
    path('signup/',views.LoginView.as_view(), name='signup'),
    path('contact/',views.ContactView.as_view(), name='contact'),
    path('job-detail/',views.JobDetails.as_view(), name='job-detail'),
    path('user-profile/',views.UserProfileView.as_view(), name='user-profile'),
]
if settings.DEBUG == False:
    print('not on debug')
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif settings.DEBUG == True:
    print('on debug')
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    print('I do not know')
