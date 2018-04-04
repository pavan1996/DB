from django.contrib.auth import views as auth_views
from django.conf.urls import url




urlpatterns = [
	url(r'^login/$', auth_views.login,{'template_name': 'registration/login1.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logout1.html'},name='logout'),
]
