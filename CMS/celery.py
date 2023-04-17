import os
from celery import Celery

# Set the default value of DJANGO_SETTINGS_MODULE so that Celery can find our Django app.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMS.settings")

# Create a Celery instance with 'CMS' as the name. This name will be used to run our Celery worker.
# E.g. >> celery app=CMS worker

app = Celery("CMS")

# Load Celery config values from our Django app settings. The namespace assures that there would be no crashes
# with other Django settings. With the namespace set, any Celery settings should be defined with the CELERY_ prefix.

app.config_from_object("django.conf.settings", namespace="CELERY")

# We should be able to discover tasks within our Django application.

"""
Any callable with shared_task would be discovered as a task.

Example:

from celery import shared_task

@shared_task
def test_task():
    print('This is a task')
    return True
"""
app.autodiscover_tasks()