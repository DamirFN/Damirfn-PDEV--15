import os
from celery import Celery

from celery.schedules import crontab    # Позволяет создавать задачу на точное определенное время

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'simpleapp.tasks.get_week_notification',
        'schedule': crontab(),
    },
}

app.autodiscover_tasks()
# hour=8, minute=0, day_of_week='mon'