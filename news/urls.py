from django.urls import path
from .views import HomePageView

app_name = 'news'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
]
