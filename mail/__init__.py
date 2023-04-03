"""
This package handles Spaceyatech blog mail services.

The package contains:
1. An email module which handles the mail logic.
2. A templates/templated_email directory which is used to register email templates.

Registering Email Templates:

Email templates are just files that are used to standardize the format and content of emails sent by the application. 
As specified in the application's settings, each email template file should have a .email extension. 

Django templating style can be used to write a template file. 

Example:

{% block subject %}My subject for {{username}}{% endblock %}
{% block plain %}
  Hi {{full_name}},

  You just signed up for my website, using:
      username: {{username}}
      join date: {{signup_date}}

  Thanks, you rock!
{% endblock %}
"""