from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', ]
        labels = {'name': 'Введите название задачи'}

    def clean_name(self):
        name = self.cleaned_data['name']
        if Task.objects.filter(name=name).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise forms.ValidationError(
                'Задача с таким названием уже существует. Пожалуйста, выберите другое название.')
        return name


class TaskAddForm(TaskForm):
    pass


class TaskEditForm(TaskForm):
    pass
