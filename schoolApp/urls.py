from . import views
from django.urls import path
app_name='schoolApp'

urlpatterns = [
    path('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('newForm',views.newForm,name='newForm'),
    path('confirm',views.confirm,name='confirm'),
    path('logoutf',views.logoutf,name='logoutf'),

]