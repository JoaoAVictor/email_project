from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.SendEmailView.as_view(), name='send-email'),
]
