import os
from mail.tasks import _async_send_email
from django.conf import settings

base_dir = os.path.abspath(os.path.dirname(__file__))

def send_email(context:dict, template:str, recipient:str) -> str:

    """
    Send templated emails to users
    this function acts as a proxy to _async_send_email

    :param context: a dict that contains info to be passed to the template
    :param template: some template
    :recipient: recipient's email address
    :return: a unique id from a scheduled task.

    usecase: suppose a user it to be send a confirmation email.

    >>> send_email(
        context={username='JohnDoe', token='sometoken'},
        template=confirmation,
        recipient='johnDoe@spaceyatech.com'
    )

    the function call schedules a task via the _async_send_email function
    and returns a unique id pointing to the given task or raise a
    FileNotFoundError if the template passed is not found in 
    ../blog/mail/templates/tempated_email/ directory
    """

    if not os.path.exists(os.path.join(base_dir,f"templates/templated_email/{template}.email")):

        raise FileNotFoundError(f"template file {template} not found")
    
    task = _async_send_email.delay(
        context=context,
        template=template,
        from_email=settings.EMAIL_HOST_USER,
        recipients=[recipient]
    )

    return task.id
