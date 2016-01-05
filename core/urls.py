from django.conf.urls import patterns, url
from core.views import NewApp, AppList

urlpatterns = patterns('core.views',
    url(r'^apps/(?P<name>[a-zA-Z0-9]+)/$', NewApp.as_view()),
    url(r'^apps/$', AppList.as_view())

)