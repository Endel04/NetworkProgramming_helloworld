from django.urls import path
from 천축 import views

app_name = '천축'

urlpatterns = [
    path('란/', views.show_란, name='하이타니 란'),
    path('린도/', views.show_린도, name='하이타니 린도'),
]