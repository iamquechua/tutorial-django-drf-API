from django.contrib import admin
from django.urls import path
from api.views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
