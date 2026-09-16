from django.urls import path
from .views import tasks_api, task_detail_api

urlpatterns = [
    path("api/tasks/", tasks_api, name="tasks_api"),
    path("api/tasks/<int:task_id>/", task_detail_api, name="task_detail_api"),
]