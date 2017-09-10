from django.conf.urls import include, url

from products import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetail.as_view())
]
