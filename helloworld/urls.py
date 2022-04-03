from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('playground/', include('playground.urls')),
    path('천축/', include('천축.urls')),
    path('admin/', admin.site.urls),
]