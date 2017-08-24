from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from core import views

urlpatterns = [
    url(r'^categoria/$', views.CategoryList.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^produto/$', views.ProductList.as_view()),
    url(r'^produto/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^supermercado/$', views.SupermarketList.as_view()),
    url(r'^supermercado/(?P<pk>[0-9]+)/$', views.SupermarketDetail.as_view()),
]
