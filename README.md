# Vouch Twitter
A web application built atop Django, that uses your twitter account for authentication, post which it can display user information, collect tweets on the authenticated user's timeline and list out the associated domains and usernames.
<br> The website is live at http://kopal.pythonanywhere.com/
# Requirements:
**Python(>=3.0)** <br>
**Django(>=3.0)**<br>
**Tweepy:** Python library to access the Twitter API <br>
**tld:** Python library to extract domain from a url <br>
# Instructions for use:
1. Clone the repository https://github.com/kchakravarty/vouch_twitter.git
2. Add your consumer key and your secret key in **utils.py** (vouch_twitter/twitter_login/login_page/utils.py). Visit https://developer.twitter.com/en to register your app.
Be sure to mention a **callback url** in the app configuration. 
3. Switch to the **twitter_login directory**(cd vouch_twitter/twitter_login). Run on localhost using python3 manage.py runserver.
# Logistics:
The web application uses **Tweepy.OAuthHAndler() for authentication**, post which the application is redirected to the callback url. 
<br>User information is accessed using the **API.me() endpoint** , and the timeline using the **API.home_timeline() endpoint** http://docs.tweepy.org/en/latest/api.html
<br> 





