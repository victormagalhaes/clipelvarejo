# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import EmailMessage


class Email(object):

	def __init__(self, data):
		self.phone = data.get('phone')
		self.message = data.get('message')
		self.name = data.get('name')
		self.email = data.get('email')
		self.is_contact = True if data.get('type') == 'contato' else False
		self.to = ['contato@clipelvarejo.com.br', ]

	def send_email(self):

		try:
			email = EmailMessage(
				subject=self._get_subject(), body=self._format_message(), from_email=settings.EMAIL_ADDRESS, to=self.to
			)
			email.content_subtype = 'html'
			email.send(fail_silently=False)
		except Exception, e:
			raise e

	def _get_subject(self):

		if self.is_contact is True:
			return "Contato - %s" % self.name
		else:
			return "Pedido/Orçamento - %s" % self.name

	def _format_message(self):

		contact = "<div>Solicitante: %s - %s</div>" % (self.name, self.phone)

		mail = "<div>Email: %s</div>" % self.email

		message = "<div>Mensagem: %s</div>" % self.message

		formatted_message = "<html>%s%s%s</html>" % (contact, mail, message)

		return formatted_message
