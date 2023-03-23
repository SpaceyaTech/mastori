from django.test import TestCase
from unittest.mock import patch
from mail.email import send_email
from django.conf import settings
# Create your tests here.

class TestMail(TestCase):

    @patch("mail.email.os", autospec=True)
    @patch("mail.email._async_send_email", autospec=True)
    def test_send_email(self, send_temp_mock, os_mock):

        recipient = "test"

        context = {}

        send_email(context=context, template="test", recipient=recipient)

        send_temp_mock.delay.assert_called_with(
            context=context,
            template="test",
            from_email=settings.EMAIL_HOST_USER,
            recipients = [recipient],
        )

        os_mock.path.exists.return_value = False

        with self.assertRaises(FileNotFoundError):

            send_email(
                context=context,
                template="test",
                recipient=recipient
            )
