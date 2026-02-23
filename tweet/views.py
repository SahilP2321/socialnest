from django.shortcuts import render
from .forms import Tweetform , UserCreationForm
from django.contrib import messages
from .models import Tweet, Like
from django.shortcuts import get_object_or_404 ,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def tweet_list(request):
    tweets = Tweet.objects.all().select_related('user').prefetch_related('likes')
    
    if request.user.is_authenticated:
        liked_tweets = Like.objects.filter(user=request.user).values_list('tweet_id', flat=True)
    else:
        liked_tweets = []
    
    return render(request, 'tweet_list.html', {
        'tweets': tweets,
        'liked_tweets': liked_tweets
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