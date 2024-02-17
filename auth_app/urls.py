from django.urls import path
from auth_app.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/login/', admin_login, name='admin_login'),
    path('logout/', logout_view, name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='auth_app/pages/password_change.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='auth_app/pages/password_change_done.html'), name='password_change_done')
]