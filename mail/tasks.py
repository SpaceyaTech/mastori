from templated_email import send_templated_mail
from celery import shared_task

@shared_task
def _async_send_email(context:dict, template:str, from_email:str, recipients:list[str]) ->None:

    """
    Schedule a task to send an email

    :param context: a dict that contains info to be passed to the template
    :param template: some template
    :param recipients: a list containing recipients' email addresses

    usage: _async_send_email.delay(context, template, from_email, recipients)

    the above call should return a unique id for the task scheduled

    the template passed should exist in the ../blog/mail/templates/tempated_email/ directory

    otherwise to handle FileNotFound exceptions on the current django process use send_email

    """

    send_templated_mail(
        from_email=from_email,
        recipient_list=recipients,
        context=context,
        template_name=template,
    )

def _error_callback():

    pass

def _success_callback():

    pass