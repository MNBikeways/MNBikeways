from django.conf.urls import patterns, include, url
from django.contrib import admin
from mapper.views import MainPage, OverpassApiAjax


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BikeMap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainPage.as_view()),
    url(r'^OSM/', OverpassApiAjax.as_view()),
)
