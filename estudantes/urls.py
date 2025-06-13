from django.urls import path
from .views import LoginView

urlpatterns = [
    path('estudantes/', LoginView.as_view(), name='estudantes_cadastro'),
]
