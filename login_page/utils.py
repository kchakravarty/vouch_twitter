import tweepy
consumer_key = 'Enter you consumer key'
consumer_secret= 'Enter yout consumer secret key'


def set_up(request):
    oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #redirect_url = auth.get_authorization_url()
    access_key = request.session['access_key_tw']
    access_secret = request.session['access_secret_tw']
    oauth.set_access_token(access_key, access_secret)
    api = tweepy.API(oauth)
    return api
