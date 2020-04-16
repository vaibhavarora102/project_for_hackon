from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='login'),
    path('login_sub',views.login_sub,name='login_sub'),
    path('disclamer',views.disclamer, name='disclamer'),
    path('form_sub',views.form_sub, name='form_sub'),
    path('spl_submit',views.spl_submit,name='spl_submit'),
]
 