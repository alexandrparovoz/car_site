
from django.contrib import admin
from django.urls import path

from worldCars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/carslist/', WorldCarsAPIView.as_view())
]
