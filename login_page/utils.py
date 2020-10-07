import tweepy
consumer_key = '4G3XqQVWviqdhkkv678mqNgMN'
consumer_secret= 'GWwgeu6nO0B8EJT4Ly9NNroq3udu0h4mRiPQJZqSRU8dJss6Sh'


def set_up(request):
    oauth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #redirect_url = auth.get_authorization_url()
    access_key = request.session['access_key_tw']
    access_secret = request.session['access_secret_tw']
    oauth.set_access_token(access_key, access_secret)
    api = tweepy.API(oauth)
    return api
