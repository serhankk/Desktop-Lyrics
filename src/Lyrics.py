import requests

class Lyrics(object):
    """Gets the lyrics of given song by the given artist."""

    def __init__(self):
        self.api_url = 'https://api.lyrics.ovh/v1'

    def get_lyrics(self, artist, song):
        response = requests.get(url=f'{self.api_url}/{artist}/{song}').json()
        try:
            return response['lyrics']
        except KeyError:
            return '''
Lyrics cannot found!
            '''



