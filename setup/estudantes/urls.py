from django.urls import path
from .views import GenerateMappingView

urlpatterns = [
    path('generate/', GenerateMappingView.as_view(), name='generate-mapping'),
]