from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from task.models import Task

urlpatterns = patterns('',
    url(r'^$', 'task.views.index', name='list_task'),
    url(r'^add/$', 'task.views.add', name='add_task'),
    url(r'^delete_multiple/$', 'task.views.delete_multiple', name='delete_multiple_task'),
    url(r'^delete/(?P<task_id>\w+)/$', 'task.views.delete', name='delete_task'),
    url(r'^update/(?P<task_id>\w+)/$', 'task.views.update_form', name='update_form_task'),
    url(r'^update/$', 'task.views.update', name='update_task'),
    url(r'^done/(?P<task_id>\w+)/$', 'task.views.done', name='done_task'),
)