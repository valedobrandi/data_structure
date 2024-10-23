from django.shortcuts import render, get_object_or_404
from django.http import Http404
from task.models import Task


# Create your views here.
def index(request):
    context = {"company": "Trybe", "tasks": Task.objects.all()}
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def task_details(request, task_id):
    try:
        task = get_object_or_404(Task, id=task_id)
        return render(request, "details.html", {"task": task})
    except Http404:
        return render(request, '404.html')