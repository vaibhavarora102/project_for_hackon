from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('privacy_policy',views.privacy_policy,name='privacy_policy'),
    path('form',views.login_sub,name='form'),
    path('disclamer',views.disclamer, name='disclamer'),
    path('result',views.form_sub, name='result'),
    path('spl_submit',views.spl_submit,name='spl_submit'),
]
 