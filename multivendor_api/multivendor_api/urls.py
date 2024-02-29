# multivendor_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('account.urls')),  # Include the "account" app's URLs
]
