from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return HttpResponse("You're at the conversion index. Use /celsius/VALUE/fahrenheit or Use fahrenheit/VALUE/celsius.")

def CelsiusGet(request, temperature):
    temperature = float(temperature)
    celsius = round((temperature - 32) / 1.8, 2)
    data = {'celsius': celsius}
    return JsonResponse(data)

def FahrenheitGet(request, temperature):
    temperature = float(temperature)
    fahrenheit = round((temperature * 1.8) + 32, 2)
    data = {'fahrenheit': fahrenheit}
    return JsonResponse(data)