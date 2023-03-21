import os
from celery import Celery

# set the default value of DJANGO_SETTINGS so that celery can find the our django app
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMS.settings")

# create Celery instance with 'celery_core' as the name. this name will be used to run our celery worker.
# eg >> cerely app=celery_core worker

app = Celery("celery_core")

# load celery config values from our django app 
# settings the namespace assures that there would be no crashes with other DJANGO settings
# with the namespace set. any celery settings should be defined with CELERY_ prefix

app.config_from_object("django.conf.settings", namespace="CELERY")

# well we should be able to discover task within our django application

"""
Any callable with shared_task would be discoverd as a task

example

from celery import shared_task

@shared_task
def test_task():

    print('this is a task')

    return True

"""
app.autodiscover_tasks()