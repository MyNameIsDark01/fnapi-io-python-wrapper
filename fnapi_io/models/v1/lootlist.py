from ..util import Images
from typing import List


class LootListV1:
    def __init__(self, data):
        self.result: bool = data.get('result')
        self.lang: str = data.get('lang')
        self.weapons: List[WeaponsV1] = [WeaponsV1(i) for i in data.get('weapons')]


class WeaponsV1:
    def __init__(self, data):
        self.id: str = data.get('id')
        self.enabled: bool = data.get('enabled')
        self.name: str = data.get('name')
        self.description: str = data.get('description')
        self.rarity: str = data.get('rarity')
        self.type: str = data.get('type')
        self.gameplay_tags: List[str] = [i for i in data.get('gameplayTags')]
        self.search_tags: str = data.get('searchTags')
        self.images: Images = Images(data.get('images'))
        self.main_stats: WeaponMainStats = WeaponMainStats(data.get('mainStats'))
        self.chances: WeaponChances = [WeaponChances(i) for i in data.get('chances')] if data.get('chances') else None


class WeaponMainStats:
    def __init__(self, data):
        self.dmb_pb: float = data.get('DmgPB')
        self.firing_rate: float = data.get('FiringRate')
        self.reload_time: float = data.get('ReloadTime')
        self.bullets_x_cartridge: float = data.get('BulletsPerCartridge')
        self.spread: float = data.get('Spread')
        self.spread_downsights: float = data.get('SpreadDownsights')
        self.damaze_zone_critical: float = data.get('DamageZone_Critical')


class WeaponChances:
    def __init__(self, data):
        self.type: str = data.get('type')
        self.chance: float = data.get('change')
        self.group: int = data.get('group')
        self.count: int = data.get('count')
