from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo'),
    path('create/', views.create, name='todo_create'),
    path('view/<int:id>', views.view, name='todo_view'),
    path('delete/<int:id>', views.delete, name='todo_delete'),
    path('edit/<int:id>', views.edit, name='todo_edit'),
]
