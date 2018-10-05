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
                {'id': todo.id,ORPI
                 'title': todo.title,
                 'completed': todo.completed
                } for todo in todos
                ]
        }
       
        return JsonResponse(data)
        
        

    def post(self, request):
        raise NotImplementedError('List POST')


class TodoDetailView(BaseCSRFExemptView):
    def get(self, request, todo_id):
        raise NotImplementedError('Detail POST')

    def delete(self, request, todo_id):
        raise NotImplementedError('Detail DELETE')

    def patch(self, request, todo_id):
        raise NotImplementedError('Detail PATCH')

    def put(self, request, todo_id):
        raise NotImplementedError('Detail PUT')
