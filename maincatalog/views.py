from django.shortcuts import render


# Create your views here.
def get_page(request, dispatcher='Catalog root'):
    context = {
        'title': dispatcher,
    }
    return render(request, 'pages/index.tpl', context)
