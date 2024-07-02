from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Mark')
    client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    
   
    location = "New York" 
    temperature = "11 degrees Celcius" 

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}! the temperature is {temperature} in {location}"
    }

    return JsonResponse(response)



