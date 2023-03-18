from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "create a super user non-interactively"


    def add_arguments(self, parser):

        parser.add_argument("--username", help="Admin's username", required=True)

        parser.add_argument("--email", help="Admin's email", required=True)

        parser.add_argument("--password", help="Admin's password", required=True)


    def handle(self, *args, **options):
        
        User = get_user_model()

        if not User.objects.filter(
            username=options['username']
        ).exists():

            User.objects.create_superuser(
                username=options['username'],
                email=options['email'],
                password=options['password']
            )