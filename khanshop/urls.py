"""khanshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import facepage.views as fp
import maincatalog.views as mc
import pages.views as pg
import userpanel.views as up

urlpatterns = [
    path('', fp.get_page, name='main_page'),
    path('catalog/', mc.get_root, name='catalog_root'),
    path('catalog/<dispatcher>', mc.get_page, name='catalog_item'),
    path('products/', mc.get_root, name='catalog_root'),
    path('products/<int:pk>', mc.get_product, name='product'),
    path('pages/', pg.get_page, name='sitemap'),
    path('pages/<dispatcher>', pg.get_page, name='other_page'),
    path('login/', up.login, name='login'),
    path('logout/', up.logout, name='logout'),
    # временно используется стандартная админка
    path('admin/', admin.site.urls),
    path('<dispatcher>', pg.get_page_by_shortcut, name='other_page'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
