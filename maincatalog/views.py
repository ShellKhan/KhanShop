from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Category


def get_ierarchy(item, step):
    res = [(item, '&nbsp;&nbsp;&nbsp;&nbsp;'*step)]
    childs = Category.objects.filter(is_active=True, parentcategory=item)
    if len(childs):
        for child in childs:
            res.extend(get_ierarchy(child, step+1))
    return res


# Create your views here.
def get_root(request):
    catlist = Category.objects.filter(is_active=True, parentcategory=None)
    ierlist = []
    for cat in catlist:
        ierlist.extend(get_ierarchy(cat, 0))
    context = {
        'title': 'Catalog root',
        'catlist': ierlist,
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
        'goods': None,
        'breadcrumbs': category.parent_list.reverse()
    }
    subcats = Category.objects.filter(is_active=True, parentcategory=category)
    if subcats:
        context['subcats'] = subcats
    return render(request, 'pages/category.tpl', context)
