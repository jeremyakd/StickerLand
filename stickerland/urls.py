from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    #path('sales/', include('sales.urls')),
    #path('', include('home.urls')),  # Suponiendo que tengas una aplicación 'home' para la página de inicio
]
