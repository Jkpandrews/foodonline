from django.urls import path
from . import views
from accounts_main import views as accountsviews

urlpatterns = [
    path('',accountsviews.venDashboard, name='vendor'),
    path('vprofile/',views.vprofile, name= 'vprofile'),

]
