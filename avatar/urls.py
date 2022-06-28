from django.urls import path
from . import views

urlpatterns = [ 

path('', views.index, name='index'),
path('video_feed',views.video_feed, name='video_feed'),
path('gender/<int:genid>/', views.character, name='character'),
path('res/<int:genid>/',views.res, name='res')

]