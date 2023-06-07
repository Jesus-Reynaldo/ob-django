from django.urls import path,include
from . import views

urlpatterns = [
    path('<letter>',views.first,name='first'),
]
