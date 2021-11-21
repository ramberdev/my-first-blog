from django.urls import path
from . import views

#связываем view под именем post_list с корневым URL-адресом ('')
urlpatterns = [
    path('', views.post_list, name='post_list'),
]