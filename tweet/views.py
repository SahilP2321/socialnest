from django.shortcuts import render
from .forms import Tweetform , UserCreationForm , Profileform
from django.contrib import messages
from .models import Tweet, Like , Profile ,Retweet
from django.shortcuts import get_object_or_404 ,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    tweets = Tweet.objects.filter(user=profile_user).select_related('user').prefetch_related('likes').order_by('-created_at')
    
    if request.user.is_authenticated:
        liked_tweets = Like.objects.filter(user=request.user).values_list('tweet_id', flat=True)
    else:
        liked_tweets = []
    
    return render(request, 'user_profile.html', {
        'profile_user': profile_user,
        'tweets': tweets,
        'liked_tweets': liked_tweets
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