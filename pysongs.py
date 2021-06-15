import requests


def searchApi(pickedSong):
    url = "https://shazam.p.rapidapi.com/search"
    querystring = {f"term": {pickedSong}}
    headers = {
        'x-rapidapi-key': "94fa715ec9msh287bb2f3ea9b3fep1ddb1cjsncf93a0131f08",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=querystring)
    return res


def suggestSongs(songKey):
    url = "https://shazam.p.rapidapi.com/songs/list-recommendations"
    querystring = {f"key": {songKey}}
    headers = {
        'x-rapidapi-key': "94fa715ec9msh287bb2f3ea9b3fep1ddb1cjsncf93a0131f08",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
        }
    res = requests.request("GET", url, headers=headers, params=querystring)
    return res


def createSongList(suggestedSongs):
    suggestedSongList = []
    for song in suggestedSongs:
        suggestedSongList.append(
            (song["track"]["title"]) + " by " + (song["track"]["subtitle"]))
    return suggestedSongList


def createListOfSuggestions(suggestedSongs):
    suggestedSongList = []
    for song in suggestedSongs:
        suggestedSongList.append((song["title"]) + " by " + (song["subtitle"]))
    return suggestedSongList


def printSongList(songList):
    counter = 1
    for song in songList:
        print(f"{counter}. {song}")
        counter += 1

pickedSong = input("Please provide a song: ")

response = searchApi(pickedSong)
suggestedSongs = response.json()["tracks"]["hits"]

suggestedSongList = createSongList(suggestedSongs)
printSongList(suggestedSongList)

reply = input("Please select a song from the above"
              "list by typing its corresponding number here: ")
reply = int(reply) - 1
associatedKey = suggestedSongs[int(reply)]["track"]["key"]

response2 = suggestSongs(associatedKey)
newSuggestedSongs = response2.json()["tracks"]
newSuggestedSongList = createListOfSuggestions(newSuggestedSongs)
printSongList(newSuggestedSongList)
