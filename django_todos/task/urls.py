from django.conf.urls import url
from task import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^list/$',views.task_list),
    url(r'^create/$',views.task_create),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.task_delete),
]