# backend/urls.py
from django.urls import path
from .views import home, try_on

urlpatterns = [
    path('', home, name='home'),
    path('try-on/', try_on, name='try_on'),  # Add the URL pattern for the try_on view
    # Add other views and URL patterns as needed
]
