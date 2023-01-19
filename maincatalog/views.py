from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Category


# Create your views here.
def get_root(request):

    context = {
        'title': 'Catalog root',
        'catlist': Category.objects.filter(is_active=True, parentcategory=None)
    }
    return render(request, 'pages/catalog.tpl', context)


def get_page(request, dispatcher=None):
    if dispatcher.isdigit():
        category = get_object_or_404(Category, pk=int(dispatcher))
    else:
        category = get_object_or_404(Category, urlname=dispatcher)
    if not category.is_visible:
        raise Http404()
    context = {
        'category': category,
        'breadcrumbs': category.parent_list
    }
    subcats = Category.objects.filter(is_active=True, parentcategory=category)
    if subcats:
        context['subcats'] = subcats
    return render(request, 'pages/category.tpl', context)
