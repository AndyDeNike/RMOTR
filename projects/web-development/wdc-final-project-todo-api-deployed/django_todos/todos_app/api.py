import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Todo


class BaseCSRFExemptView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class TodoListView(BaseCSRFExemptView):
    def get(self, request):
        #raise NotImplementedError('List GET')
        todos = Todo.objects.all()
        status = request.GET.get('status', 'all')
        
        if status == 'active':
            todos = todos.filter(completed=False)
        elif status == 'completed':
            todos = todos.filter(completed=True)
        
        data = {
            'filter': status,
            'count': todos.count(),
            'results': [
                {'id': todo.id,
                 'title': todo.title,
                 'completed': todo.completed
                } for todo in todos
                ]
        }
       
        return JsonResponse(data)
        
        

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        if 'title' not in data:
            return JsonResponse({}, status=400)
        title = data['title']
        completed = data.get('completed', False)
        
        Todo.objects.create(title=title, completed=completed)
        return JsonResponse({}, status=201)


class TodoDetailView(BaseCSRFExemptView):
    def get(self, request, todo_id):
        #raise NotImplementedError('Detail POST')
        todo = get_object_or_404(Todo, id=todo_id)
        data = {
            'id': todo.id,
            'title': todo.title,
            'completed': todo.completed
        }
        return JsonResponse(data)

    def delete(self, request, todo_id):
        #raise NotImplementedError('Detail DELETE')
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()
        return HttpResponse(status=204)
        

    def patch(self, request, todo_id):
        raise NotImplementedError('Detail PATCH')

    def put(self, request, todo_id):
        #raise NotImplementedError('Detail PUT')
        todo = get_object_or_404(Todo, id=todo_id)
        data = json.loads(request.body.decode('utf-8'))
        for field in ['title', 'completed']:
            if field not in data:
                return JsonResponse({'error': 'Missing argument: {}'.format(field)}, status=400)
            setattr(todo, field, data[field])
            #todo[field] = data[field]
            todo.save()
        return HttpResponse(status=204)
            
                
