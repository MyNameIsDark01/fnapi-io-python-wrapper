from typing import List


class AchievementsV1:
    def __init__(self, data):
        self.result: bool = data.get('result')
        self.season: int = data.get('season')
        self.achievements: List[Achievement] = [Achievement(i) for i in data.get('achievements')]


class Achievement:
    def __init__(self, data):
        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.description: str = data.get('description')
        self.total: int = data.get('total')
        self.image: str = data.get('image')
