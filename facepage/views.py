from django.shortcuts import render


# Create your views here.
def get_page(request):
    context = {
        'title': 'Main Page',
    }
    return render(request, 'pages/index.tpl', context)
