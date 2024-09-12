from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm
import json
# Create your views here.

@api_view(['GET'])
def GetTask(request, id):
        try:
                task = Task.objects.get(pk=id)

                data = {
                        'id': task.id,
                        'name': task.name,
                        'maked as done': task.done 
                }
                return JsonResponse({ "response": "Get task", 'task': data})
        except Task.DoesNotExist:
                return Http404("Item not found")
@api_view(['POST'])
def CreateTask(request):
        try:
                data = json.loads(request.body)
                form =  TaskForm(data)

                if form.is_valid():
                        task = form.save()
                        response = {
                                "message": "Task created",
                                "task": {
                                        'id': task.id,
                                        'name': task.name,
                                        'done': task.done
                                }
                        }
                        return JsonResponse(response)
                else:
                        return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status = 400)

@api_view(['PUT'])
def UpdateTask(request, id):
        try:    
                data = json.loads(request.body)
                form =  TaskForm(data)
                task = Task.objects.get(pk=id)
                

        except Task.DoesNotExist:
                return JsonResponse({'error': 'Task not found'}, status = 404)
        return JsonResponse({"response": "Update task"})   

@api_view(['DELETE'])
def DeleteTask(request, id):
        print('id ----->', id)
        try:
                task = Task.objects.get(pk=id)
                task.delete()
                return JsonResponse({"message": "Deleted task",
                                     "task": {
                                        'id': id,
                                        'name': task.name,
                                        'done': task.done
                                } })
        except Task.DoesNotExist:
                return JsonResponse({'error': f'Task with id {id},  NOT FOUND'}, status = 404)
        

@api_view(['GET'])
def GetAll(request):
        tasksResponse = []
        tasks = Task.objects.all()
        for task in tasks:
                tasksResponse.append({ "id": task.id, "task name": task.name, "task is done": task.done})
        return JsonResponse({ "response": "Get All", 'tasks': tasksResponse})
