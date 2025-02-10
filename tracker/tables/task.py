import django_tables2 as tables
from tracker.models import Task


class TaskTable(tables.Table):
    name_template = "<a href='{% url 'edit_task' record.pk %}'>{{ record.name }}</a>"
    name = tables.TemplateColumn(name_template, verbose_name="Название задачи")
    time_spent = tables.Column(orderable=False, verbose_name="Время затраченное",
                               attrs={"td": {"id": lambda record: f"time-spent-{record.pk}"}})
    state = tables.Column(orderable=False, verbose_name='Состояние')
    total_time = tables.Column(orderable=False, verbose_name='Общее время выполнения')

    class Meta:
        model = Task
        fields = ('name', 'state', 'time_spent', 'total_time')
        template_name = "django_tables2/bootstrap.html"
