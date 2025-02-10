import pytest
from tracker.models import Task


@pytest.mark.django_db
def test_task_creation():
    task = Task.objects.create(name="Test Task")
    assert task.name == "Test Task"
    assert task.status == "active"
    assert task.start_time is not None


@pytest.mark.django_db
def test_task_mark_as_completed():
    task = Task.objects.create(name="Test Task")
    task.mark_as_completed()
    assert task.status == "completed"
    assert task.duration_seconds is not None


@pytest.mark.django_db
def test_task_mark_as_paused():
    task = Task.objects.create(name="Test Task")
    task.mark_as_paused()
    assert task.status == "paused"
    assert task.duration_seconds is not None


@pytest.mark.django_db
def test_task_mark_as_active():
    task = Task.objects.create(name="Test Task", status="paused")
    task.mark_as_active()
    assert task.status == "active"
    assert task.start_time is not None


@pytest.mark.django_db
def test_task_time_spent():
    task = Task.objects.create(name="Test Task")
    assert task.time_spent is not None


@pytest.mark.django_db
def test_task_total_time():
    task = Task.objects.create(name="Test Task")
    task.mark_as_completed()
    assert task.total_time is not None