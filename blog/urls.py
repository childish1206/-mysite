from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
# 這是網址路由設定