# cartvista/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),  # Include the backend app's URLs
    # Add a default route to handle the root path
    path('', include('backend.urls')),  # You can replace 'backend.urls' with your desired app's URL pattern
]
