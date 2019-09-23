from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def happyhappyjoyJoy(request):
    return HttpResponse("Cruising the town")


def gogettheGoods(request):
    return HttpResponse("Here you go! almost finish")