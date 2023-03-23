import os
from mail.tasks import _async_send_email
from django.conf import settings

base_dir = os.path.abspath(os.path.dirname(__file__))

def send_email(context:dict, template:str, recipient:str) -> str:

    """
    Send templated emails to users.
    This function acts as a proxy to `_async_send_email`.

    :param context: A dictionary that contains information to be passed to the template.
    :param template: A string that represents the name of the template to be used for the email.
    :param recipient: A string that represents the email address of the recipient.
    :return: A unique ID from a scheduled task.

    Use case: Suppose a user is to be sent a confirmation email.

    Example usage:
    >>> send_email(
            context={'username': 'JohnDoe', 'token': 'sometoken'},
            template='confirmation',
            recipient='johnDoe@spaceyatech.com'
        )

    The function call schedules a task via the `_async_send_email` function
    and returns a unique ID pointing to the given task or raises a
    `FileNotFoundError` if the template passed is not found in the
    `../blog/mail/templates/templated_email/` directory.
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
