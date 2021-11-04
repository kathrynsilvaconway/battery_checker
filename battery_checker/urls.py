from django.urls import path, include

urlpatterns = [
    path('', include('battery_app.urls')),
]
