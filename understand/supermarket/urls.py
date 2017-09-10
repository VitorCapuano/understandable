from django.conf.urls import url

from supermarket import views

urlpatterns = [
    url(r'^$', views.SupermarketList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SupermarketDetail.as_view()),
    url(r'^(?P<pk>[0-9]+)/produtos/$', views.supermarket_list)
]
