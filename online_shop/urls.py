from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # Root urls
    path('', include('home.urls', namespace='home')),
    path('', include('accounts.urls', namespace='accounts')),
]
