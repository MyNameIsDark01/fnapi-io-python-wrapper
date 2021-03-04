from ..util import LastUpdate, TransInfo, Images


class CosmeticListV2:
    def __init__(self, data):
        self.result = data.get('result')
        self.lang = data.get('lang')
        self.items_count = data.get('itemsCount')
        self.items = [CosmeticV2(i) for i in data.get('items')]


class UpcomingCosmeticsV2:
    def __init__(self, data):
        self.result = data.get('result')
        self.last_update = LastUpdate(data.get('lastUpdate'))
        self.items = [CosmeticV2(i) for i in data.get('items')]


class ItemDetailsV2:
    def __init__(self, data):
        self.result = data.get('result')
        self.item = CosmeticV2(data.get('item'))


class CosmeticV2:
    def __init__(self, data):
        self.id = data.get('id')
        self.type = TransInfo(data.get('type')) if 'type' in data else None
        self.name = data.get('name')
        self.description = data.get('description')
        self.rarity = TransInfo(data.get('rarity')) if 'rarity' in data and data.get('rarity') else None
        self.series = TransInfo(data.get('series')) if 'series' in data and data.get('series') else None
        self.price = data.get('price')
        self.added = AddedV2(data.get('added')) if 'added' in data else None
        self.built_in_emote = CosmeticV2(data.get('buildInEmote')) if 'buildInEmote' in data else None
        self.copyrighted_audio = data.get('copyrightedAudio')
        self.upcoming = data.get('upcoming')
        self.reactive = data.get('reactive')
        self.release_date = data.get('releaseDate')
        self.last_appearance = data.get('lastAppearence')
        self.interest = data.get('interest')
        self.images = Images(data.get('images'))
        self.video = data.get('video')
        self.gameplay_tags = data.get('gameplayTags')
        self.battlepass = data.get('battlepass')
        self.set = TransInfo(data.get('set')) if 'set' in data and data.get('set') else None


class AddedV2:
    def __init__(self, data):
        self.date = data.get('date')
        self.version = data.get('version')


class BPInfoV2:
    def __init__(self, data):
        self.season = data.get('season')
        self.tier = data.get('tier')
        self.type = data.get('type')
        self.display_text = BPTextV2(data.get('displayText'))
        self.battle_pass_name = data.get('battlePassName')


class BPTextV2:
    def __init__(self, data):
        self.chapter = data.get('chapter')
        self.season = data.get('season')
        self.chapter_season = data.get('chapterSeason')
