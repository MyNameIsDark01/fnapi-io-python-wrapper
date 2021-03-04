from ..util import LastUpdate, TransInfo
from .cosmetic import CosmeticV2


class ShopV2:
    def __init__(self, data):
        self.result = data.get('result')
        self.full_shop = data.get('fullShop')
        self.last_update = LastUpdate(data.get('lastUpdate'))
        self.current_rotation = data.get('currentRotation')
        self.next_rotation = data.get('nextRotation')
        self.carousel = (data.get('carousel'))
        self.shop = [ShopCosmetics(i) for i in data.get('shop')]


class ShopCosmetics:
    def __init__(self, data):
        self.display_name = data.get('displayName')
        self.display_description = data.get('displayDescription')
        self.display_type = data.get('displayType')
        self.main_type = data.get('mainType')
        self.offer_id = data.get('offerId')
        self.display_assets = [DAv2(i) for i in data.get('displayAssets')]
        self.first_release_date = data.get('firstReleaseDate')
        self.previous_release_date = data.get('previousReleaseDate')
        self.gift_allowed = data.get('giftAllowed')
        self.buy_allowed = data.get('buyAllowed')
        self.price = ShopPrice(data.get('price'))
        self.rarity = TransInfo(data.get('rarity')) if data.get('rarity') else None
        self.series = TransInfo(data.get('series')) if data.get('series') else None
        self.banner = TransInfo(data.get('banner')) if data.get('banner') else None
        self.granted = [CosmeticV2(i) for i in (data.get('granted'))]
        self.priority = data.get('priority')
        self.section = TransInfo(data.get('section'))
        self.group_index = data.get('groupIndex')
        self.store_name = data.get('storeName')
        self.tile_size = data.get('tileSize')
        self.categories = [i for i in data.get('categories')]


class ShopPrice:
    def __init__(self, data):
        self.regular_price = data.get('regularPrice')
        self.final_price = data.get('finalPrice')


class ShopCarousel:
    def __init__(self, data):
        self.title = data.get('title')
        self.url = data.get('url')
        self.offer_id = data.get('offerId')


class DAv2:
    def __init__(self, data):
        self.url: str = data.get('url')
        self.background: str = data.get('background')
        self.render_data: dict = data.get('renderData')
