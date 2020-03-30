from spotipy import util, Spotify


class SpotifyApiDataFetcher(object):

    def __init__(self, user_id, user_credentials):
        self.user_id = user_id
        self.credentials = user_credentials
        oauth_token = self._get_oauth_token()
        self.spotify = Spotify(auth=oauth_token)

    def _get_oauth_token(self):
        client_id = self.credentials.get('client_id')
        client_secret_key = self.credentials.get('client_secret')
        credential_client = util.oauth2.SpotifyClientCredentials(client_id, client_secret_key)
        return credential_client.get_access_token()

    def get_user_playlist_ids(self):
        user_playlists = self.spotify.user_playlists(user=self.user_id)
        return [item['id'] for item in user_playlists['items']]

    def get_playlist_content(self):
        pass

    def get_user_favorite_songs(self):
        pass


if __name__ == '__main__':
    fetcher = SpotifyApiDataFetcher(user_id=user_id, user_credentials=credentials)
