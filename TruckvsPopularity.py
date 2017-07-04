import re
import requests
import urllib.request
from bs4 import BeautifulSoup
from bottle import route, run, request
import spotipy
import sys
from spotipy import oauth2
import spotipy.util as util

PORT_NUMBER = 8080
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'
print(len(sys.argv))
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()
token = util.prompt_for_user_token(username,SCOPE,client_id='311940949ffb4afd98de6284b46fc15b',client_secret='2f654b5b80104d15826b041335485813',redirect_uri='http://localhost:8080')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)
# sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )

# @route('/')
# def index():

#     access_token = ""

#     token_info = sp_oauth.get_cached_token()

#     if token_info:
#         print ("Found cached token!")
#         access_token = token_info['access_token']
#     else:
#         url = request.url
#         code = sp_oauth.parse_response_code(url)
#         if code:
#             print ("Found Spotify auth code in Request URL! Trying to get valid access token...")
#             token_info = sp_oauth.get_access_token(code)
#             access_token = token_info['access_token']

#     if access_token:
#         print ("Access token available! Trying to get user information...")
#         sp = spotipy.Spotify(access_token)
#         results = sp.current_user()
#         return results

#     else:
#         return htmlForLoginButton()

# def htmlForLoginButton():
#     auth_url = getSPOauthURI()
#     htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
#     return htmlLoginButton

# def getSPOauthURI():
#     auth_url = sp_oauth.get_authorize_url()
#     return auth_url

# run(host='', port=8080)
name = "asking alexandria"
spotify = spotipy.Spotify()
results = spotify.search(q='artist:' + name, type='artist')
print(results)
 
def get_lyrics(artist,song_title):
    artist = artist.lower()
    song_title = song_title.lower()
    # remove all except alphanumeric characters from artist and song_title
    artist = re.sub('[^A-Za-z0-9]+', "", artist)
    song_title = re.sub('[^A-Za-z0-9]+', "", song_title)
    if artist.startswith("the"):    # remove starting 'the' from artist e.g. the who -> who
        artist = artist[3:]
    url = "http://azlyrics.com/lyrics/"+artist+"/"+song_title+".html"
    
    try:
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)
        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('</br>','').replace('</div>','').strip()
        return lyrics
    except Exception as e:
        return "Exception occurred \n" +str(e)

lyrics = get_lyrics("Asking Alexandria", "Another Bottle Down")
# print(lyrics)