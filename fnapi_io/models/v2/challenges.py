from .cosmetic import CosmeticV2
from ..util import XYLocation


class ChallengesV2:
    def __init__(self, data):
        self.result = data.get('result')
        self.season = data.get('season')
        self.lang = data.get('lang')
        self.bundles = [MissionBundles(i) for i in data.get('bundles')]


class MissionBundles:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.type = data.get('unlockType')
        self.tags = data.get('tags')
        self.colors = data.get('colors')
        self.images = data.get('images')
        self.bundle_reward = [CosmeticV2(i) for i in data.get('bundleRewards')]
        self.quests = [Quest(i) for i in data.get('quests')]


class Quest:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.enabled = data.get('enabled')
        self.parent_quest = data.get('parentQuest')
        self.progress_total = data.get('progressTotal')
        self.tags = data.get('tags')
        self.reward = QuestReward(data.get('reward'))
        self.locations = [QuestLocation(i) for i in data.get('locations')]


class QuestReward:
    def __init__(self, data):
        self.xp = data.get('xp')
        self.items = [CosmeticV2(i) for i in data.get('items')]


class QuestLocation:
    def __init__(self, data):
        self.tag = data.get('tag')
        self.location = XYLocation(data.get('location')) if 'location' in data and data.get('location') else None
