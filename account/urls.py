from django.conf.urls import url
# from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from . import views

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login', logout_then_login, name='logout-then-login'),
    url(r'^$', views.dashboard, name='dashboard'),
    # Widoki zmiany hasła
    url(r'^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # Widoki resetu hasła
    # Umożliwienie wysłania linku do zmiany hasła
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    # Potwierdzenie wysłania maila z linkiem
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # Zdefiniowanie nowego hasła
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Informacja o poprawnym ustaleniu nowego hasła
    url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
