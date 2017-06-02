from django.conf.urls import url
from . import views


app_name = 'app'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^sessions/$', views.SessionList.as_view(), name='session_list'),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='session_detail'),
    url(r'sessions/add/$', views.SessionCreate.as_view(), name='session_add'),
    url(r'^sessions/(?P<pk>[0-9]+)/update/$', views.SessionUpdate.as_view(), name='session_update'),
    url(r'^sessions/(?P<pk>[0-9]+)/delete/$', views.SessionDelete.as_view(), name='session_delete'),



]