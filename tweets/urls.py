from django.urls import path

from . import views

app_name = 'tweets'

urlpatterns = [
    path('', views.TweetList.as_view(), name='tweet_list'),
	
	path('create/', views.CreateTweet.as_view(), name='create_tweet'),

	# path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
]
