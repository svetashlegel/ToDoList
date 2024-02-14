from tasks.apps import TasksConfig
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from tasks.views import TaskViewSet

app_name = TasksConfig.name


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls
