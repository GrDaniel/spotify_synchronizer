from spotipy import util, Spotify


class Client(object):

    def __init__(self, user_id, user_credentials):
        self.user_id = user_id
        self.credentials = user_credentials
        self.token = self._get_oauth_token()

    def _get_oauth_token(self):
        client_id = self.credentials.get('client_id')
        client_secret_key = self.credentials.get('client_secret')
        credentials_client = util.oauth2.SpotifyClientCredentials(client_id, client_secret_key)
        return credentials_client.get_access_token()

    def authorize(self):
        return Spotify(auth=self.token)
