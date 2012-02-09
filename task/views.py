from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from task.models import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    task_list = Task.objects.all()
    form = TaskForm()
    return render_to_response('task/index.html', RequestContext(request, {'task_list': task_list, 'form': form}))

def add(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('list_task'))

def delete_multiple(request):
    if request.POST.get('action_type') == 'delete':
        Task.objects.filter(pk__in = request.POST.getlist('tasks')).delete()
    elif request.POST.get('action_type') == 'done':
        Task.objects.filter(pk__in = request.POST.getlist('tasks')).update(done=True)
    elif request.POST.get('action_type') == 'notdone':
        Task.objects.filter(pk__in = request.POST.getlist('tasks')).update(done=False)
    return HttpResponseRedirect(reverse('list_task'))

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('list_task'))

#if request.method == 'POST':
def update_form(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(instance=task)
    return render_to_response('task/update.html', RequestContext(request, {'task_id':task_id,'form': form}))

def update(request):
    task = get_object_or_404(Task, pk=request.POST.get('id'))
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('list_task'))

def done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = True
    task.save()
    return HttpResponseRedirect(reverse('list_task'))