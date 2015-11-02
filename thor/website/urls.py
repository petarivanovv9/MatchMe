from django.conf.urls import url

from .views import index, user_register, user_login, user_logout

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^register/$', user_register, name="register"),
    url(r'^login/$', user_login, name="login"),
    url(r'^logout/$', user_logout, name="logout"),
]
