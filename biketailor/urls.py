from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biketailor.views.home', name='home'),
    # url(r'^biketailor/', include('biketailor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="home.html")),

    url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html")),

    url(r'^meme/$', TemplateView.as_view(template_name="meme.html")),
)
