from typing import List


class RadiosV1:
    def __init__(self, data):
        self.result: bool = data.get('result')
        self.lang: str = data.get('lang')
        self.ratios: List[Radio] = [i for i in data.get('radios')]


class Radio:
    def __init__(self, data):
        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.enabled: bool = data.get('enabled')
        self.icon: str = data.get('icon')
        self.versions: List[RadioVersion] = [RadioVersion(i) for i in data.get('versions')]


class RadioVersion:
    def __init__(self, data):
        self.version: int = data.get('version')
        self.url: str = data.get('url')
