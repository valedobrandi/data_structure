from django.urls import path
from task.views import index, about, task_details

urlpatterns = [
    path("", index, name="home-page"),
    path("about", about, name="about-page"),
    path("tasks/<int:task_id>", task_details, name='details-page')
]
