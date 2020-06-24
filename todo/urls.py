from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('del_todo/<int:todo_id>/', views.del_todo, name='del_todo'),
]