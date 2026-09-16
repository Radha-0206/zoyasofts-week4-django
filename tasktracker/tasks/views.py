from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json


@csrf_exempt
def tasks_api(request):

    # GET - Show all tasks
    if request.method == "GET":
        tasks = Task.objects.all()

        data = []

        for task in tasks:
            data.append({
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date,
            })

        return JsonResponse({
            "tasks": data
        })

    # POST - Add a new task
    elif request.method == "POST":
        data = json.loads(request.body)

        task = Task.objects.create(
            task_name=data["task_name"],
            description=data["description"],
            status=data["status"]
        )

        return JsonResponse({
            "message": "Task created successfully",
            "task": {
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status
            }
        }, status=201)

    return JsonResponse({
        "message": "Method not allowed"
    }, status=405)


@csrf_exempt
def task_detail_api(request, task_id):

    try:
        task = Task.objects.get(id=task_id)

    except Task.DoesNotExist:
        return JsonResponse({
            "error": "Task not found"
        }, status=404)

    # PUT - Update task
    if request.method == "PUT":

        data = json.loads(request.body)

        task.task_name = data["task_name"]
        task.description = data["description"]
        task.status = data["status"]

        task.save()

        return JsonResponse({
            "message": "Task updated successfully",
            "task": {
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status
            }
        })

    # DELETE - Delete task
    elif request.method == "DELETE":

        task.delete()

        return JsonResponse({
            "message": "Task deleted successfully"
        })

    return JsonResponse({
        "message": "Method not allowed"
    }, status=405)