# -*- coding: utf-8 -*-
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
			email = EmailMessage(subject=self.subject, body=self._format_message(), from_email=self.email, to=self.to)
			email.send(fail_silently=False)
		except Exception, e:
			raise e

	def _format_message(self):

		contact = "<div>Contato: %s - %s</div>" % (self.name, self.phone)

		message = "<div>%s</div>" % self.message

		formatted_message = "<html>%s%s</html>" % (contact, message)

		return formatted_message
