from django.conf.urls import url

from partner import views

urlpatterns = [
    url(r'^$', views.PartnerList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.PartnerDetail.as_view())
]
