from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from usuarios.views import router as myapp_router

api = NinjaAPI()
api.add_router("/api/", myapp_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls),
]