from django.conf.urls import include, url

from products import views

urlpatterns = [
    url(r'^produto/$', views.ProductList.as_view()),
    url(r'^produto/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view())
]
