from django.test import TestCase
from unittest.mock import patch
from mail.email import send_email
# Create your tests here.

class TestMail(TestCase):

    @patch("mail.email.os", autospec=True)
    @patch("mail.email._async_send_email", autospec=True)
    def test_send_email(self, send_temp_mock, os_mock):

        recipients = ["test"]

        context = {}

        send_email(context=context, template="test", recipients=recipients)

        send_temp_mock.delay.assert_called_with(
            context=context,
            template="test",
            recipients = recipients,
        )

        os_mock.path.exists.return_value = False

        with self.assertRaises(FileNotFoundError):

            send_email(context=context, template="test", recipients=recipients)
