from django.shortcuts import render


# Create your views here.
def get_page(request, dispatcher='Site map'):
    context = {
        'title': dispatcher,
    }
    return render(request, 'pages/page.tpl', context)
