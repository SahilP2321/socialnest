from . import views
from django.urls import path
urlpatterns = [
    path('',views.tweet_list,name="tweet_list"),
    path('create/',views.tweet_create,name="tweet_create"),
    path('<int:tweet_id>/delete/',views.tweet_delete,name="tweet_delete"),
    path('<int:tweet_id>/edit/',views.tweet_edit,name="tweet_edit"),
    path('register/', views.register,name="register"),
    path('like/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('unlike/<int:tweet_id>/', views.unlike_tweet, name='unlike_tweet'),
    path('profile/',views.profile,name="profile"),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('retweet/<int:tweet_id>',views.retweet_tweet,name="retweet"),
    path('unretweet/<int:tweet_id>',views.unretweet_tweet,name="unretweet"),
    path('follow/<str:username>',views.follow,name="follow"),
    path('unfollow/<str:username>',views.unfollow,name="unfollow"),

]