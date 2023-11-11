from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey="AIzaSyDWRH3IC7hklbhzPbR61vTpjwp9D8zVAiw")
        self.title = self.youtube['items'][0]['snippet']['title']
        self.video_count = int(self.youtube['items'][0]['statistics']['videoCount'])
        self.description = self.youtube['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'
    def __str__(self):
        return f'{self.title}({self.url})'

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        return self.subscriber_count != other.subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        youtube = build('youtube', 'v3', developerKey="AIzaSyDWRH3IC7hklbhzPbR61vTpjwp9D8zVAiw")
        return youtube

    def to_json(self, filename):
        """
        Сохраняет в файл значения атрибутов экземпляра `Channel`
        """
        with open(filename, 'w', encoding='utf-8') as file:
            information = {
                "id канала": self.channel_id,
                "Название канала": self.title,
                "Описание канала": self.description,
                "ссылка на канал": self.url,
                "количество подписчиков": self.subscriber_count,
                "количество видео": self.video_count,
                "общее количество просмотров": self.view_count
            }
            json.dump(information, file, ensure_ascii=False)

