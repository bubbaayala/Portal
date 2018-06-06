from django.conf.urls import url
from . import views

app_name = 'App'

urlpatterns = [
    #/App/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/App/<app_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/App/app/add
    url(r'app/add/$', views.AppCreate.as_view(), name='app-add'),

    #/App/app/app_id
    url(r'app/(?P<pk>[0-9]+)/$', views.AppUpdate.as_view(), name='app-update'),

    #/App/app/app_id/delete
    url(r'app/(?P<pk>[0-9]+)/delete/$', views.AppDelete.as_view(), name='app-delete'),

    #/App/<app.id>/detailadd
    url(r'^(?P<pk>[0-9]+)/detailcreate$', views.appdetail_add, name='appdetail-create'),
]
