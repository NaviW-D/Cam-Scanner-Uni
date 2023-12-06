from django.urls import path
from .views import get_car_tag_status
urlpatterns = [
    path("<str:tag>",get_car_tag_status)
]