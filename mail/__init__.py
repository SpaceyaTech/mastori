"""
This Package handles spaceyatech blog mail services.

The Package contains 1. email module which handles the mail logic
                     2. templates/templated_email directory which is used to register email templates

Registering Email templates

email templates are just files that are used ......

as specied in the applications settings each email template file should have a .email extention

Django templating style can be used to write a template file. 

example

{% block subject %}My subject for {{username}}{% endblock %}
{% block plain %}
  Hi {{full_name}},

  You just signed up for my website, using:
      username: {{username}}
      join date: {{signup_date}}

  Thanks, you rock!
{% endblock %}

"""