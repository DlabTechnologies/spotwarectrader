from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('withdraw_not_eligable/', views.withdraw_not_eligable, name='withdraw_not_eligable'),
    path('withdraw_complete_error/', views.withdraw_complete_error, name='withdraw_complete_error'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('deposit/', views.deposit, name='deposit'),
    path('deposit_complete/', views.deposit_complete, name='deposit_complete'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('user_profile/', views.user_profile, name='user_profile'),

    
    path('deposit_history/', views.deposit_history, name='deposit_history'),
    path('withdraw_history/', views.withdraw_history, name='withdraw_history'),
    path('dashboard_contact/', views.dashboard_contact, name='dashboard_contact'),

    path('account_types', views.account_types, name='account_types'),
    path('register', views.Signup_view, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    
    path('validate_otp', views.validate_phone_otp, name='validate_otp'),
    path('send_otp', views.send_otp, name='send_otp'),
    path('account_upgrade', views.send_upgrade_email, name='account_upgrade'),
    path('change_email_address', views.change_email_address, name='change_email_address'),
    path('identity_verification', views.identity_verification, name='identity_verification'),
    path('identity_verification_complete', views.identity_verification_complete, name='identity_verification_complete'),
    path('identity_verification_proceed', views.identity_verification_proceed, name='identity_verification_proceed'),


     # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), 
        name='password_change'),
    
    #password reset 
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
     name='password_reset_complete'),
]


urlpatterns += staticfiles_urlpatterns()