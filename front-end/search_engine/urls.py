from django.conf.urls import url

from . import views

# urlpatterns = [
#         url(r'^$', views.index, name='index'),
#         url(r'^(?P<search_word>.+)/$', views.results,
#             name='results'),
#         ]

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),)

