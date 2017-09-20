from django.conf.urls import url

from cart import views

urlpatterns = [
    url(r'^$', views.CreateCart.as_view()),
    url(r'^adicionar/$', views.ProductsToCart.as_view())
]
