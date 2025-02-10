from .forms import TaskEditForm, TaskAddForm
from .models import Task
from django_tables2 import SingleTableView
from django.views.generic import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .tables.task import TaskTable
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse


class TaskBaseView:
    model = Task
    success_url = reverse_lazy('task_list')


class TaskAddView(TaskBaseView, CreateView):
    form_class = TaskAddForm
    template_name = 'tracker/add_task.html'


class TaskUpdateView(TaskBaseView, UpdateView):
    form_class = TaskEditForm
    template_name = 'tracker/edit_task.html'


class TaskDeleteView(TaskBaseView, DeleteView):
    pass


class TaskListView(SingleTableView):
    model = Task
    template_name = "tracker/task_list.html"
    table_class = TaskTable
    paginate_by = 15


class TaskCompleteView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.mark_as_completed()
        return redirect('task_list')


class TaskPauseView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.mark_as_paused()
        return redirect('task_list')


class TaskContinueView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.mark_as_active()
        return redirect('task_list')


def get_time_spent(request):
    task_ids = request.GET.get('task_ids').split(',')
    task_ids = [int(task_id) for task_id in task_ids if task_id]
    times_dict = {}
    if task_ids:
        # Получаем время для каждой задачи по ID.
        tasks_query_set = Task.objects.filter(id__in=task_ids)
        for task in tasks_query_set:
            times_dict[task.id] = task.time_spent
    return JsonResponse({'times': times_dict})
