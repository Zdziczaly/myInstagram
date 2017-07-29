from django.conf.urls import url
# from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from . import views

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login', logout_then_login, name='logout-then-login'),
    url(r'^$', views.dashboard, name='dashboard')
]
