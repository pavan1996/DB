from django.contrib.auth import views as auth_views
from django.conf.urls import url 
from .views import student

urlpatterns = [
    
    url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'},name='logout'),
    url(r'^student/$', student, name='student'),
]
