from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


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


def get_page(request, dispatcher):
    if dispatcher.isdigit():
        category = get_object_or_404(Category, pk=int(dispatcher))
    else:
        category = get_object_or_404(Category, urlname=dispatcher)
    if not category.is_visible:
        raise Http404()
    context = {
        'category': category,
        'breadcrumbs': reversed(category.parent_list)
    }
    if subcats := Category.objects.filter(
        is_active=True, parentcategory=category
    ):
        context['subcats'] = subcats
    if products := Product.objects.filter(category_id=category):
        context['products'] = products
    return render(request, 'pages/category.tpl', context)


def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not product.is_active or not product.category.is_visible:
        raise Http404()
    breadcrumbs = [product.category] + product.category.parent_list
    print(breadcrumbs)
    main_image = None
    if gallery := product.get_images.filter(is_active=True):
        main_image = product.get_images.get(is_main=True) or gallery[0]
    context = {
        'breadcrumbs': reversed(breadcrumbs),
        'product': product,
        'gallery': gallery,
        'main_image': main_image,
    }
    return render(request, 'pages/product.tpl', context)
