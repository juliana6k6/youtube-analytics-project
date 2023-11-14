import os
from datetime import timedelta
import isodate
from googleapiclient.discovery import build


class PlayList():

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.youtube = build('youtube', 'v3', developerKey="AIzaSyA1AdjSyGNFqyG7mnhHB3yuX0DmHu0fgrI")
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.playlists = self.youtube.playlists().list(channelId=playlist_id, part='contentDetails,snippet',
                                                       maxResults=50, ).execute()
        self.title = self.playlist_videos['items'][0]['snippet']['localized']['title']
        self.url = f"https://www.youtube.com/playlist?list=/{self.playlist_id}"
