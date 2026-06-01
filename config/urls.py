from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-test/', include('api.urls')),
    path('api/', include('motostore.views.urls')),
]
