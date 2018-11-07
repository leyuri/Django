# video/urls.py
from django.conf.urls import url, include
from . import views

app_name = 'video'

urlpatterns = [
    url(r'^$', views.video_list, name='list'),

    url(r'^new$', views.video_new, name='new'),
      # 이 코드를 추가해 주세요
    url(r'^(?P<video_id>\d+)/$', views.video_detail, name='detail'),
]