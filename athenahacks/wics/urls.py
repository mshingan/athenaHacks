from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^signup/$', views.add_client,name='add_client'),
    url(r'^confirm/$', views.confirm,name='confirm'),
]
