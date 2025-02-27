import datetime

import geocoder
import requests
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

def temp_here(request):
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    location = geocoder.ip('me').latlng
    api_request = f'{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m&temperature_unit=fahrenheit'
    now = datetime.datetime.now()
    hour=now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]

    return HttpResponse(f'Temperature at your location is {temp}°F')


def factorial_with_cache(request, n):
    n = int(n)

    # Check if the result is already in the cache
    result = cache.get(f'factorial_{n}')

    if result is None:
        # If not in the cache, calculate the factorial
        result = 1
        for i in range(1, n + 1):
            result *= i
        cache.set(f'factorial_{n}', result, 60)  # Cache for 60 seconds

    return HttpResponse(f'Factorial of {n} is: {result}')