from django.conf.urls import include, url

urlpatterns = [
    url(r'^categoria/', include('category.urls')),
    url(r'^produto/', include('products.urls')),
    url(r'^supermercado/', include('supermarket.urls'))
]
