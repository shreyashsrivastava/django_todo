from django.shortcuts import render
from . import models
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.

def base(request):
    todo_list = models.todo.objects.all().order_by('-id')

    for_front = {
        'todo_list':todo_list,
    }
    return render(request, 'base.html', for_front)

def add_todo(request):
    date = timezone.now()
    text = request.POST['content']
    models.todo.objects.create(date=date, text=text)
    return HttpResponseRedirect('/')

def del_todo(request, todo_id):
    models.todo.objects.get(id=todo_id).delete()
    
    return HttpResponseRedirect('/')
    