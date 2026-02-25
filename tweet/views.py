from django.shortcuts import render
from .forms import Tweetform , UserCreationForm , Profileform
from django.contrib import messages
from .models import Tweet, Like , Profile ,Retweet , Follow
from django.shortcuts import get_object_or_404 ,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    return render(request, 'home.html')

def tweet_list(request):
    tweets = Tweet.objects.all().select_related('user').prefetch_related('likes', 'retweets')
    
    if request.user.is_authenticated:
        liked_tweets = Like.objects.filter(user=request.user).values_list('tweet_id', flat=True)
        retweeted_tweets = Retweet.objects.filter(user=request.user).values_list('tweet_id', flat=True)
    else:
        liked_tweets = []
        retweeted_tweets = []
    
    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'liked_tweets': liked_tweets,
        'retweeted_tweets': retweeted_tweets,
    })

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = Tweetform(request.POST , request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Tweetform()
    return render(request,"tweet_form.html",{"form":form})

@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method == "POST":
        form = Tweetform(request.POST , request.FILES , instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = Tweetform(instance=tweet)
    return render(request,"tweet_form.html",{"form":form})

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,"tweet_confirm_delete.html",{"tweet":tweet})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   # no need commit=False
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    
    like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)
    
    if created:
        messages.success(request, f"You liked @{tweet.user.username}'s tweet!")
    
    return redirect(request.META.get('HTTP_REFERER', 'tweet_list'))

@login_required
def unlike_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    
    # Remove like
    like = Like.objects.filter(user=request.user, tweet=tweet)
    if like.exists():
        like.delete()
        messages.success(request, f"You unliked @{tweet.user.username}'s tweet!")
    
    return redirect(request.META.get('HTTP_REFERER', 'tweet_list'))

@login_required
def profile(request):
    user_profile , create = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = Profileform(request.POST,request.FILES,instance=user_profile)
        if form.is_valid():
            form.save()  
            return redirect('profile') 
    else:
        form = Profileform(instance=user_profile)
    return render(request,"profile.html", {"form": form})


def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    
    # Get user's own tweets
    own_tweets = Tweet.objects.filter(user=profile_user).select_related('user').prefetch_related('likes', 'retweets')
    
    # Get tweets this user retweeted
    retweeted_tweet_ids = Retweet.objects.filter(user=profile_user).values_list('tweet_id', flat=True)
    retweeted_tweets = Tweet.objects.filter(id__in=retweeted_tweet_ids).select_related('user').prefetch_related('likes', 'retweets')
    
    # Combine and order by date
    from itertools import chain
    from operator import attrgetter
    
    all_tweets = list(chain(own_tweets, retweeted_tweets))
    all_tweets.sort(key=attrgetter('created_at'), reverse=True)
    
    # Get liked tweets for authenticated user
    if request.user.is_authenticated:
        liked_tweets = Like.objects.filter(user=request.user).values_list('tweet_id', flat=True)
        retweeted_by_user = Retweet.objects.filter(user=request.user).values_list('tweet_id', flat=True)
        
        # CHECK IF CURRENT USER FOLLOWS THIS PROFILE USER
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()
    else:
        liked_tweets = []
        retweeted_by_user = []
        is_following = False
    
    followers_count = Follow.objects.filter(following=profile_user).count()
    following_count = Follow.objects.filter(follower=profile_user).count()
    
    return render(request, 'user_profile.html', {
        'profile_user': profile_user,
        'tweets': all_tweets,
        'liked_tweets': liked_tweets,
        'retweeted_tweets': retweeted_by_user,
        'is_following': is_following,          # ← MAKE SURE THIS IS HERE
        'followers_count': followers_count,     # ← MAKE SURE THIS IS HERE
        'following_count': following_count,     # ← MAKE SURE THIS IS HERE
    })

@login_required
def retweet_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    retweet, created = Retweet.objects.get_or_create(user=request.user, tweet=tweet)
    
    if created:
        messages.success(request, f"You retweeted @{tweet.user.username}'s tweet!")
    else:
        messages.info(request, f"You already retweeted this tweet!")
    
    return redirect(request.META.get('HTTP_REFERER', 'tweet_list'))

@login_required
def unretweet_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    retweet = Retweet.objects.filter(user=request.user, tweet=tweet)
    
    if retweet.exists():
        retweet.delete()  
        messages.success(request, f"Removed retweet of @{tweet.user.username}'s tweet!")
    else:
        messages.info(request, f"You hadn't retweeted this!")
    
    return redirect(request.META.get('HTTP_REFERER', 'tweet_list'))

@login_required
def follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    
    if request.user == user_to_follow:
        messages.error(request, "You cannot follow yourself")
        return redirect('tweet_list')  
    
    already_following = Follow.objects.filter(
        follower=request.user,
        following=user_to_follow
    ).exists()  
    if already_following:
        messages.info(request, f"You are already following @{username}")
        return redirect('tweet_list')
    else:
        follower = Follow(follower=request.user,
               following = user_to_follow)
        follower.save()
        messages.success(request,f"Successfully followed @{username}")
        return redirect("tweet_list")

@login_required
def unfollow(request,username):
    user_to_unfollow = get_object_or_404(User,username=username)
    if request.user == user_to_unfollow:
        messages.error(request, "You cannot unfollow yourself")
        return redirect('tweet_list')
    follow = Follow.objects.filter(
        follower = request.user,
        following = user_to_unfollow
    )
    if follow.exists():
        follow.delete()
        messages.success(request,"Follower Removed")
    else:
        messages.error(request,"Follower already removed")


    
