import datetime
import isodate
from googleapiclient.discovery import build


class PlayList:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.youtube = build('youtube', 'v3', developerKey="AIzaSyA1AdjSyGNFqyG7mnhHB3yuX0DmHu0fgrI")
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        self.playlists_info = self.youtube.playlists().list(channelId=playlist_id, part='contentDetails,snippet',
                                                       maxResults=50,
                                                       ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(self.video_ids)
                                               ).execute()
        self.title = self.playlists_info['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list=/{self.playlist_id}"

    @property
    def total_duration(self):
        """возвращает объект класса datetime.timedelta с суммарной длительностью плейлиста """
        total_dur = datetime.timedelta()
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_dur += duration
        return total_dur

    def show_best_video(self):
        """Возвращает ссылку на самое популярное видео из плейлиста по количеству лайков"""
        max_likes = 0
        max_likes_video_id = ""
        for video in self.video_response['items']:
            like_count = int(video['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                max_likes_video_id = video['id']
        return f'https://youtu.be/{max_likes_video_id}'
