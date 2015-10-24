from django.shortcuts import render

# Create your views here.
def home(request):
    # View code here...
    title = 'Clipel Varejo'

    context = {
        'title': title
    }

    return render(request, 'base.html', context)
