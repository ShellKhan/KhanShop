from django.shortcuts import render


# Create your views here.
# поиск по айди или урлу
def get_page(request, dispatcher='Site map'):
    context = {
        'title': dispatcher,
    }
    return render(request, 'pages/page.tpl', context)


# поиск по короткой ссылке
def get_page_by_shortcut(request, dispatcher):
    context = {
        'title': dispatcher,
    }
    return render(request, 'pages/page.tpl', context)
