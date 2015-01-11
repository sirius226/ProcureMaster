from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from procuremaster.views import index, hello, current_datetime, hours_ahead, display_meta

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'procuremaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',index),
    url(r'^coming-soon/$',index),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^meta/$', display_meta),
    url(r'^admin/', include(admin.site.urls)),
)
