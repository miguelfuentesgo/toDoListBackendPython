from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .forms import TaskForm
import json
from django.shortcuts import get_object_or_404

# Views

@api_view(['GET'])
def GetTask(request, id):
        try:
                task = Task.objects.get(pk=id)
                
                data = {
                        'id': task.id,
                        'description': task.description,
                        'completed': task.completed 
                }
                return JsonResponse({ "response": "getTask", 'task': data})
        except Task.DoesNotExist:
                return JsonResponse({'error': f'Task with id {id},  NOT FOUND'}, status = 404)
@api_view(['POST'])
def CreateTask(request):
        try:
                data = json.loads(request.body)
                form =  TaskForm(data)

                if form.is_valid():
                        task = form.save()
                        task.completed = False
                        response = {
                                "response": "createTask",
                                "task": {
                                        'id': task.id,
                                        'description': task.description,
                                        'completed': task.completed
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
        except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        try:
                task = Task.objects.get(pk=id)
                form = TaskForm(data, instance=task)
                if form.is_valid():
                        form.save()
                        return JsonResponse({"message": "updateTask",  "task":{
                                "id": task.id,
                                "description": task.description,
                                "completed": task.completed
                        }})  
        except Task.DoesNotExist:
                return JsonResponse({'error': f'Task with id {id},  NOT FOUND'}, status = 404)

@api_view(['DELETE'])
def DeleteTask(request, id):
        try:
                task = Task.objects.get(pk=id)
                task.delete()
                return JsonResponse({"response": "deleteTask",
                                     "task": {
                                        'id': id,
                                        'description': task.description,
                                        'completed': task.completed
                                } })
        except Task.DoesNotExist:
                return JsonResponse({'error': f'Task with id {id},  NOT FOUND'}, status = 404)
        

@api_view(['GET'])
def GetAll(request):
        tasksResponse = []
        tasks = Task.objects.all()
        for task in tasks:
                tasksResponse.append({ "id": task.id, "description": task.description, "completed": task.completed})
        return JsonResponse({ "response": "getAll", 'tasks': tasksResponse})
