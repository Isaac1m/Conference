
from django.conf.urls import url, include
from django.contrib import admin
import app.views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', app_views.login, name='login'),
    url(r'^logout/', app_views.logout, name='logout'),
    url(r'^conference/', include('app.urls')),
    url(r'^$', app_views.index, name='main_index'),

]
