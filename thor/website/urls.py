from django.conf.urls import url

from .views import index, user_register, user_login, user_logout
from .views import view_event


urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^register/$', user_register, name="register"),
    url(r'^login/$', user_login, name="login"),
    url(r'^logout/$', user_logout, name="logout"),

    url(r'^event/(?P<event_id>\d+)/$', view_event, name="event"),
]
