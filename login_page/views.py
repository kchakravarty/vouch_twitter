# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login_page.utils import *
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
import tweepy
from django.http import HttpResponse, HttpResponseRedirect
import os
from tld import get_tld

# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def check(request):
    return render(request, 'login.html')

def info(request):
    access_key = request.session.get('access_key_tw', None)
    print(access_key)
    api=set_up(request)
    user = api.me()
    #print(user)
    return render(request,'info.html', {'user' : user})


def auth(request):
    oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = oauth.get_authorization_url(True)
    response = HttpResponseRedirect(auth_url)
    request.session['request_token'] = oauth.request_token
    return response

def callback(request):
	verifier = request.GET.get('oauth_verifier')
	oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	token = request.session.get('request_token')
	# remove the request token now we don't need it
	request.session.delete('request_token')
	oauth.request_token = token
	# get the access token and store
	try:
		oauth.get_access_token(verifier)
	except tweepy.TweepError:
		print('Error, failed to get access token')

	request.session['access_key_tw'] = oauth.access_token
	request.session['access_secret_tw'] = oauth.access_token_secret
	#print(request.session['access_key_tw'])
	#print(request.session['access_secret_tw'])
	response = HttpResponseRedirect(reverse('check'))
	return response

def tweets(request):
    access_key = request.session.get('access_key_tw', None)
    api=set_up(request)
    statuses = api.home_timeline(tweet_mode='extended')
    return render(request, 'tweets.html', {'statuses': statuses})

def domain(request):
    access_key = request.session.get('access_key_tw', None)
    api=set_up(request)
    statuses = api.home_timeline(tweet_mode='extended')
    user=[]
    domain=[]
    for status in statuses:
        user.append(status.user.screen_name)
        for t in status.entities['urls']:
            res=get_tld(t['expanded_url'],as_object=True)
            domain.append(res.domain)
    freq_domain = max(set(domain), key = domain.count)
    freq_user = max(set(user) , key= user.count)

    return render(request, 'domain.html', {'domains':set(domain),'users': set(user),'freq_domain':freq_domain,'freq_user':freq_user})
