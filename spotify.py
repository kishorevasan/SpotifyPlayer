import requests
import json
import webbrowser


headers = {
    'Accept': 'application/json',
}

    
def play(user_query,query_type):
    temp_query = user_query.split()
    query = ''.join( x + '+' for x in temp_query)
    query = query[:len(query)-1]
    r = requests.get('https://api.spotify.com/v1/search?q='+query+'&type='+query_type+'&limit=1', headers=headers)
    jSON = r.json()
    print jSON
    if(query_type == 'track'):
        webbrowser.open(jSON["tracks"]["items"][0]["external_urls"]["spotify"])
    elif(query_type=='artist'):
        webbrowser.open(jSON["artists"]["items"][0]["external_urls"]["spotify"])
    elif(query_type == 'album'):
        webbrowser.open(jSON["albums"]["items"][0]["external_urls"]["spotify"])
    else: #query_type == 'playlist'
        webbrowser.open(jSON["playlists"]["items"][0]["external_urls"]["spotify"])
