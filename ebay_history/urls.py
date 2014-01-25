from django.conf.urls import patterns, include, url

from views import HomeView, SimilarView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^similar/$', SimilarView.as_view(), name='similar'),

    url(r'^admin/', include(admin.site.urls)),
)
