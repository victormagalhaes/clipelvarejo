# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import EmailMessage


class Email(object):

	def __init__(self, data):

		self.phone = data.get('phone')
		self.message = data.get('message')
		self.name = data.get('name')
		self.email = data.get('email')
		self.subject = 'Contato do site Clipel Varejo'
		self.to = ['dandaim@gmail.com', ]

	def send_email(self):

		try:
			email = EmailMessage(
				subject=self.subject, body=self._format_message(), from_email=settings.EMAIL_ADDRESS, to=self.to
			)
			email.content_subtype = 'html'
			email.send(fail_silently=False)
		except Exception, e:
			raise e

	def _format_message(self):

		contact = "<div>Contato: %s - %s</div>" % (self.name, self.phone)

		mail = "<div>Email: %s</div>" % self.email

		message = "<div>%s</div>" % self.message

		formatted_message = "<html>%s%s%s</html>" % (contact, mail, message)

		return formatted_message
