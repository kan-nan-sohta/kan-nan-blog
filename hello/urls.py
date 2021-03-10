from django.urls import path, include
from . import views


app_name = 'blog'

urlpatterns = [
        path('', views.index, name='index'),
        path('detail/<int:blog_id>/', views.detail, name='detail'),
]