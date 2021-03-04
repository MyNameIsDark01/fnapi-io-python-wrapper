from ..util import TransInfo
from typing import List


class ItemSetsV1:
    def __init__(self, data):
        self.result: bool = data.get('result')
        self.lang: str = data.get('lang')
        self.sets: List[TransInfo] = [TransInfo(i) for i in data.get('sets')]
