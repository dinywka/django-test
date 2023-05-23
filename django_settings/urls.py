from django.contrib import admin
from django.urls import path, include
from django_ads_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_ads_app.urls')),
]
