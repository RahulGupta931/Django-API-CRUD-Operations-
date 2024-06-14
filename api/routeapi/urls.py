from django.urls import path
from main.views import *

urlpatterns = [
    path('get-person/', get_person),
    path('save-person/', save_person),
    path('save-car/', save_car),
    path('get-car/', get_car)

]