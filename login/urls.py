from django.urls import path
from .views import groukamloginview,homelistview

urlpatterns = [
    path('login/',groukamloginview.as_view(), name='login'),
    path('home/', homelistview.as_view(), name='home')
    
]
