from templated_email import send_templated_mail
from celery import shared_task
from celery.signals import task_failure

@shared_task
def _async_send_email(context:dict, template:str, from_email:str, recipients:list[str]) ->None:

    """
    Schedule a task to send an email asynchronously.

    Args:
        context (dict): A dictionary containing information to be passed to the email template.
        template (str): The name of the email template file.
        from_email (str): The email address of the sender.
        recipients (list[str]): A list of email addresses of the recipients.

    Usage:
        _async_send_email.delay(context, template, from_email, recipients)

    Returns:
        None.

    Note:
        The "send_templated_mail" function is used to send the email using the provided information. 
        This function is asynchronous and runs in the background, which allows the application to continue processing 
        without waiting for the email to be sent.
    """

    send_templated_mail(
        from_email=from_email,
        recipient_list=recipients,
        context=context,
        template_name=template,
    )

def _on_mail_error_callback(sender=None, task_id=None, exeption=None, **kwargs):

    # This function is a placeholder for handling errors that may occur during email sending. 
    # It is not yet implemented, so it currently does nothing. 

    # However, the plan is to eventually use a global application logging service to log any errors that occur during email sending. 

    pass


task_failure.connect(_on_mail_error_callback, sender=_async_send_email)