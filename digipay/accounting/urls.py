from django.urls import path
from . import views

app_name= 'account'
urlpatterns = [
    path('account/', views.RegisterView.as_view(), name='account'),  
]