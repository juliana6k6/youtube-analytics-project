import os
from googleapiclient.discovery import build
from src.channel import Channel


class Video(Channel):
    """
    Класс для видеоролика
    """
    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.video_info = build('youtube', 'v3', developerKey="AIzaSyDWRH3IC7hklbhzPbR61vTpjwp9D8zVAiw")
        self.title = self.video_info['items'][0]['snippet']['title']
        self.video_count = int(self.video_info['items'][0]['statistics']['videoCount'])
        self.url = f'https://www.youtube.com/channel/{self.video_id}'
        self.view_count = int(self.video_info['items'][0]['statistics']['viewCount']

class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id


