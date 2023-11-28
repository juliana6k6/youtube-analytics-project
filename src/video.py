import os
from googleapiclient.discovery import build
from src.channel import Channel


class Video():
    """
    Класс для видеоролика
    """
    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        try:

            self.youtube = build('youtube', 'v3', developerKey="AIzaSyDWRH3IC7hklbhzPbR61vTpjwp9D8zVAiw")
            self.video_info = self.youtube.videos().list(id=self.video_id, part="snippet,statistics").execute()
            self.title = self.video_info['items'][0]['snippet']['title']
            self.like_count = int(self.video_info['items'][0]['statistics']['likeCount'])
            self.url = f'https://www.youtube.com/channel/{self.video_id}'
            self.view_count = int(self.video_info['items'][0]['statistics']['viewCount'])
        except IndexError:
            self.url = None
            self.title = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return self.title

class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id



