from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('playground/', include('playground.urls')),
    path('admin/', admin.site.urls),
]