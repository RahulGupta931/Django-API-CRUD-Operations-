from django.contrib import admin
from django.urls import path,include
from routeapi.urls import *

urlpatterns = [
    path('api/', include('routeapi.urls')),
    path('admin/', admin.site.urls),
]
