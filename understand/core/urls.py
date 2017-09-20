from django.conf.urls import include, url

urlpatterns = [
    url(r'^categoria/', include('category.urls')),
    url(r'^produto/', include('products.urls')),
    url(r'^supermercado/', include('supermarket.urls')),
    url(r'^parceiro/', include('partner.urls')),
    url(r'^cliente/', include('client.urls')),
    url(r'^carrinho/', include('cart.urls'))
]
