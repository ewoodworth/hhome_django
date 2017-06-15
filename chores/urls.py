from django.conf.urls import url

from .views import (
    ChoreCreate, ChoreDelete, ChoreUpdate, chore_list, chore_detail)

"""URL patterns that map the chores portion of HappyHome. 
   format: url(regex, view, name)"""

urlpatterns = [
    url(r'^tag/$',
        chore_list,
        name='chores_chore_list'),
    url(r'^chore/create/$',
        ChoreCreate.as_view(),
        name='chores_chore_create'),
    url(r'^chore/(?P<slug>[\w\-]+)/$',
        chore_detail,
        name='chores_chore_detail'),
    url(r'^chore/(?P<slug>[\w-]+)/delete/$',
        ChoreDelete.as_view(),
        name='chores_chore_delete'),
    url(r'^chore/(?P<slug>[\w\-]+)/update/$',
        ChoreUpdate.as_view(),
        name='chores_chore_update'),
]