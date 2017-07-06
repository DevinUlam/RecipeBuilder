
import requests
# import urllib.request
# from bs4 import BeautifulSoup
# from bottle import route, run, request
# import spotipy
# import sys
# from spotipy import oauth2
# import spotipy.util as util
import getToken
import lyriccomparison
from collections import defaultdict

# SPOTIPY_CLIENT_ID = '311940949ffb4afd98de6284b46fc15b'
# SPOTIPY_CLIENT_SECRET = '2f654b5b80104d15826b041335485813'
# SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
# PORT_NUMBER = 8080
# SCOPE = 'user-library-read'
# CACHE = '.spotipyoauthcache'
#
# sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )
#
# @route('/')
# def index():
#
#     access_token = ""
#
#     token_info = sp_oauth.get_cached_token()
#
#     if token_info:
#         print ("Found cached token!")
#         access_token = token_info['access_token']
#         print(access_token)
#     else:
#         url = request.url
#         code = sp_oauth.parse_response_code(url)
#         if code:
#             print ("Found Spotify auth code in Request URL! Trying to get valid access token...")
#             token_info = sp_oauth.get_access_token(code)
#             access_token = token_info['access_token']
#
#     if access_token:
#         print ("Access token available! Trying to get user information...")
#         sp = spotipy.Spotify(access_token)
#         results = sp.current_user()
#         return results
#
#     else:
#         return htmlForLoginButton()
#
# def htmlForLoginButton():
#     auth_url = getSPOauthURI()
#     htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
#     return htmlLoginButton
#
# def getSPOauthURI():
#     auth_url = sp_oauth.get_authorize_url()
#     return auth_url

#run(host='localhost', port=8888)

topArtists = {
    "Chris Stapleton": {
        "key": "4YLtscXsxbVgi031ovDDdh",
        "popularity": 1
    },
    "Blake Shelton": {
        "key": "1UTPBmNbXNTittyMJrNkvw",
        "popularity": 2
    },
    "Florida Georgia Line": {
        "key": "3b8QkneNDz4JHKKKlLgYZg",
        "popularity": 3
    },
    "Thomas Rhett": {
        "key": "6x2LnllRG5uGarZMsD4iO8",
        "popularity": 4
    },
    "Carrie Underwood": {
        "key": "4xFUf1FHVy696Q1JQZMTRj",
        "popularity": 5
    },
    "Luke Bryan": {
        "key": "0BvkDsjIUla7X0k6CSWh1I",
        "popularity": 6
    }
}

token = getToken.getToken()


albumdict = {}
songdict = {}
countdict = {}
i = 0
for artist in topArtists:

    artistID = topArtists[artist]['key']

    #request info about each artist
    artistrequest = requests.get("https://api.spotify.com/v1/artists/{0}".format(artistID), headers={"Authorization": "Bearer {0}".format(token)})
    artistinfo = artistrequest.json()

    # request the albums of each artist
    albumrequest = requests.get("https://api.spotify.com/v1/artists/{0}/albums".format(artistID), headers={"Authorization": "Bearer {0}".format(token)})
    albumdata = albumrequest.json()
    albumdict.update({'Artist{0}'.format(i): {}})
    albumdict['Artist{0}'.format(i)].update({'Name': artist})

    songdict.update({'Artist{0}'.format(i): {}})
    songdict['Artist{0}'.format(i)].update({'name': artist})

    countdict['Artist'] = artist
    countdict['numtruck'] = 0
    countdict['numbeer'] = 0

    j=0
    #print(albumdata)
    for items in albumdata['items']:
        #print(albumdict)
        #print(items)
        #print(j)
        if j > 0:
            if items['name'] != albumdict['Artist{0}'.format(i)]['Album{0}'.format(j-1)]:
                if items['album_type'] != "compilation":

                    albumdict['Artist{0}'.format(i)].update({'Album{0}'.format(j): items['name']})
                    albumdict['Artist{0}'.format(i)].update({'Album{0}ID'.format(j): items['uri'].replace("spotify:album:", "")})
                    albumdict['Artist{0}'.format(i)].update({'Popularity': artistinfo['popularity']})
                    albumdict['Artist{0}'.format(i)].update({'Followers': artistinfo['followers']['total']})


                    albumID = albumdict['Artist{0}'.format(i)]['Album{0}ID'.format(j)]
                    songrequest = requests.get("https://api.spotify.com/v1/albums/{0}/tracks".format(albumID), headers={"Authorization": "Bearer {0}".format(token)})
                    songdata = songrequest.json()


                    for songs in songdata['items']:

                        count = lyriccomparison.getLyrics(artist, songs['name'])


                        if count['truck'] != 0:

                            newtruck = countdict['numtruck'] + 1

                            countdict.update({'numtruck': newtruck})
                            print(countdict)
                        elif count['beer'] != 0:
                            newbeer = countdict['numbeer'] + 1
                            countdict.update({'numbeer': newbeer})
                            print(countdict)


                    #k=k+1

                    j = j + 1
        else:
            if items['album_type'] != "compilation":
                albumdict['Artist{0}'.format(i)].update({'Album{0}'.format(j): items['name']})
                albumdict['Artist{0}'.format(i)].update({'Album{0}ID'.format(j): items['uri'].replace("spotify:album:", "")})
                albumdict['Artist{0}'.format(i)].update({'Popularity': artistinfo['popularity']})
                albumdict['Artist{0}'.format(i)].update({'Followers': artistinfo['followers']['total']})
                albumID = albumdict['Artist{0}'.format(i)]['Album{0}ID'.format(j)]
                #print(albumID)
                j = j + 1


    #print(i)


        #print("artistID =", artistID)
        #print(albumdict['Artist{0}'.format(i)]['Album{0}ID'.format(i)])

    i = i + 1
print(countdict)
#print(songdict)
# k=0
# for album in albumdict:
#     print(album)
#     k = k + 1
#lyriccomparison.getSongList(albumdict)
#print(albumdict)
#countTruck = lyriccomparison.getLyrics("Asking Alexandria", "Another Bottle Down")

#print(countTruck)