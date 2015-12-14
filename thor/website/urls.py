from django.conf.urls import url

from .views import index, user_register, user_login, user_logout
from .views import view_event, attend_event
from .views import view_profile, edit_profile


urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^register/$', user_register, name="register"),
    url(r'^login/$', user_login, name="login"),
    url(r'^logout/$', user_logout, name="logout"),

    url(r'^event/(?P<event_id>\d+)/$', view_event, name="event"),
    url(r'^event/attend/(?P<event_id>\d+)/$', attend_event, name="attend"),


    url(r'^profile/$', view_profile, name="profile"),
    url(r'^profile/edit/$', edit_profile, name="edit"),
]
