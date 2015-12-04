import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from base.mail import Email
from base.models import DestaquePrincipal, DestaqueSecundario, Servico, Produto


def home(request):
	# View code here...
	title = 'Clipel Varejo'

	destaques_principais = DestaquePrincipal.objects.all()
	destaque_secundario = DestaqueSecundario.objects.filter(ativo=True)
	servicos = Servico.objects.all().order_by('-updated_at')
	produtos = Produto.objects.all().order_by('-updated_at')


	context = {
		'title': title,
		'destaques_principais': destaques_principais,
		'destaque_secundario_um': destaque_secundario[0],
		'destaque_secundario_dois': destaque_secundario[1],
		'servicos': servicos,
		'produtos': produtos,
	}

	return render(request, 'base.html', context)


@csrf_exempt
def mail(request):
	data = request.POST

	result = {
		'success': 'true'
	}

	if data:
		email = Email(data)
		email.send_email()
	else:
		result['success'] = 'false'

	return HttpResponse(json.dumps(result), content_type='application/json')
