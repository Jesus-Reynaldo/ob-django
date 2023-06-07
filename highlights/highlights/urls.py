
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/',include('messages.urls')),
    path('optional/',include('optional_parameters.urls')),
    path('first/',include('first_letter.urls')),
]
