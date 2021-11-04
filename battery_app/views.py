from django.shortcuts import render, redirect
import psutil

def index(request):
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    context = {
        'result': percent
    }
    print("CCOOOOOOOOOOOWWWWW", type(percent))
    return render(request, 'index.html', context)

# Create your views here.
