from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^proposals', views.proposals),
    url(r'^help', views.help),
    url(r'^signup', views.signup),
    url(r'^support/(?P<user_id>\d+)/(?P<proposal_id>\d+)', views.support),
    url(r'^user_is_supporting/(?P<user_id>\d+)/(?P<proposal_id>\d+)', views.user_is_supporting),
    url(r'^user_can_support/(?P<user_id>\d+)/(?P<proposal_id>\d+)', views.user_can_support),
    url(r'^get_remaining_budget/(?P<user_id>\d+)', views.get_remaining_budget),

    url('^login$', auth_views.login, {'template_name': 'signup_login.html'}),
    url('^logout', auth_views.logout, {'template_name': 'signup_login.html'}),
]