# NOTE: this example requires PyAudio because it uses the Microphone class
import speech_recognition as sr
import requests
import json
import spotify

# obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

spotify_auth = "BQAkWyXBZ9rxuD9rgGZp-9eHh3QOfJ7Tgm0LoLg1yw20YFx6XVoWDu236mG-i3BQzd-PXNXQDdnVSAAIQ01VjrnVq2fPHVHmlgGDJ2JR0gD2TCH-ygfKddPF2ZgqXQWB1FFckaWZ9KgE03Wlh7r5NG3HdLK6-XXR2sOYJsvAxbnDMi2y9rBMigGnWCQ"
# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "9ee2c67ba31a44b6a79cf0fb97419937" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
LUIS_KEY = 'ecb89bb426324f5da92a00a07fd7729c'

try:
    text = r.recognize_bing(audio,key = BING_KEY)
    print text
    query = ''.join(x +"%20" for x in text.split())
    r = requests.get('https://api.projectoxford.ai/luis/v2.0/apps/45262d9e-4ddb-44e2-9670-ed11ba65e348?subscription-key='+LUIS_KEY+'&q='+query+'&verbose=true')
    jSON = r.json()
    intent = jSON["topScoringIntent"]["intent"]
    entity = jSON["topScoringIntent"]["actions"][0]["parameters"][0]["value"][0]["entity"]
    query_type = 'track'#default search type for intent None
    if(intent=='PlaySong'):
        query_type = 'track'
    elif(intent == 'PlayAlbum'):
        query_type = 'album'
    elif(intent=='PlayArtist'):
        query_type = 'artist'
    elif(intent == 'PlayPlaylist'):
        query_type = 'playlist'
    spotify.play(entity,query_type)

except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
