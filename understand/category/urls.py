from django.conf.urls import include, url

from category import views

urlpatterns = [
    url(r'^categoria/$', views.CategoryList.as_view()),
    url(r'^categoria/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
]
