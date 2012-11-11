from django.conf.urls import patterns, url

urlpatterns = patterns('votes.views',
    url(r'^$', 'index'),
    url(r'^(?P<machine_id>\d+)/$', 'detail'),
    url(r'^(?P<machine_id>\d+)/result/$', 'result'),
    url(r'^(?P<machine_id>\d+)/edit/$', 'edit'),
)
