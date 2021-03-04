from datetime import datetime


class LastUpdate:
    def __init__(self, data):
        self.date: datetime = data.get('date')
        self.uid: str = data.get('uid')


class TransInfo:
    def __init__(self, data):
        self.id: str = data.get('id')
        self.name: str = data.get('name')
        self.intensity: str = data.get('intensity')
        self.landing_priority: int = data.get('landingPriority')
        self.part_of: str = data.get('partOf')


class Images:
    def __init__(self, data):
        self.icon: str = data.get('icon')
        self.featured: str = data.get('featured')
        self.background: str = data.get('background')
        self.full_background: str = data.get('full_background')


class XYLocation:
    def __init__(self, data):
        self.x: int = data.get('x')
        self.y: int = data.get('y')
