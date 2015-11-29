from django.shortcuts import render
from base.models import DestaquePrincipal, DestaqueSecundario, Servico, Produto

# Create your views here.
def home(request):
    # View code here...
    title = 'Clipel Varejo'

    destaque_principal = DestaquePrincipal.objects.filter(is_principal=True)[0]
    destaque_secundario = DestaqueSecundario.objects.filter(ativo=True)
    servicos = Servico.objects.all().order_by('-updated_at')
    produtos = Produto.objects.all().order_by('-updated_at')

    context = {
        'title': title,
        'destaque_principal': destaque_principal,
        'destaque_secundario_um': destaque_secundario[0],
        'destaque_secundario_dois': destaque_secundario[1],
        'servicos': servicos,
        'produtos': produtos,
    }

    return render(request, 'base.html', context)
