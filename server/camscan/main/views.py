from django.shortcuts import render
from django.http import JsonResponse
from .models import CarTag
# Create your views here.


def get_car_tag_status(request,tag):
    car = CarTag.objects.filter(tag=tag)
    if car:=car[0] :
        return(JsonResponse({"tag":tag,"status":car.availability,"expiration":car.expiration_time}))
    else :
        return(JsonResponse({"details":"car tag not find"},status=404))
