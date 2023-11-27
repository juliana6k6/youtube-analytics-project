from googleapiclient.discovery import build
import json


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey="AIzaSyA1AdjSyGNFqyG7mnhHB3yuX0DmHu0fgrI")
        self.response1 = self.youtube.channels().list(id=self.channel_id, part="snippet,statistics").execute()
        self.title = self.response1['items'][0]['snippet']['title']
        self.video_count = int(self.response1['items'][0]['statistics']['videoCount'])
        self.description = self.response1['items'][0]['snippet']['description']
        self.subscriber_сount = int(self.response1["items"][0]["statistics"]["subscriberCount"])
        self.url = f'https://www.youtube.com/channel/{self.channel_id}'

    def __str__(self):
        return f'{self.title}({self.url})'

    def __gt__(self, other):
        return self.subscriber_сount > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_сount >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_сount < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_сount <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_сount == other.subscriber_count

    def __ne__(self, other):
        return self.subscriber_сount != other.subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        info = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        youtube = build('youtube', 'v3', developerKey="AIzaSyA1AdjSyGNFqyG7mnhHB3yuX0DmHu0fgrI")
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
                "количество подписчиков": self.subscriber_сount,
                "количество видео": self.video_count,
                "общее количество просмотров": self.video_count
            }
            json.dump(information, file, ensure_ascii=False)
