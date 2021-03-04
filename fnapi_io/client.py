from .http import SyncRequest
from .models.v1.achievements import AchievementsV1
from .models.v1.cosmetic import ItemSetsV1
from .models.v1.lootlist import LootListV1
from .models.v2.challenges import ChallengesV2
from .models.v2.cosmetic import CosmeticListV2, UpcomingCosmeticsV2, ItemDetailsV2
from .models.v2.shop import ShopV2


class FortniteApi:
    def __init__(self, api_key: str):
        """
        Set FortniteApi Object and HTTPS Request with api_key

        :param api_key: You can get it on https://dashboard.fortniteapi.io/
        """

        self.api_key = api_key
        self.http = SyncRequest()
        self.http.add_header('Authorization', self.api_key)

    def get_challenges(self, language: str = 'en', season: str = 'current') -> ChallengesV2:
        """
        Get Fortnite Challenges

        :param language: supported languages
        :param season: current / older
        :return: ChallengesV2 object
        """

        params = {'lang': language, 'season': season}
        data = self.http.get('v2/challenges', params=params)
        return ChallengesV2(data)

    def get_items(self, language: str = 'en') -> CosmeticListV2:
        """
        Get a list of all fortnite items

        :param language: supported languages
        :return: CosmeticListV2 object
        """

        params = {'lang': language}
        data = self.http.get('v2/items/list', params=params)
        return CosmeticListV2(data)

    def get_upcoming_items(self, language: str = 'en') -> UpcomingCosmeticsV2:
        """
        Get upcoming items

        :param language: supported languages
        :return: UpcomingCosmeticV2 object
        """

        params = {'lang': language}
        data = self.http.get('v2/items/upcoming', params=params)
        return UpcomingCosmeticsV2(data)

    def get_item_details(self, item_id: str, language: str = 'en') -> ItemDetailsV2:
        """
        Get Item Details by item ID

        :param item_id: id of item you want to search
        :param language: supported languages
        :return: ItemDetailsV2 object
        """

        params = {'id': item_id, 'lang': language}
        data = self.http.get('v2/items/get', params=params)
        return ItemDetailsV2(data)

    def get_list_of_sets(self, language: str = 'en') -> ItemSetsV1:
        """
        Get list of all sets that are in Fortnite

        :param language: supported languages
        :return: ItemSetsV1 object
        """

        params = {'lang': language}
        data = self.http.get('v1/items/sets', params=params)
        return ItemSetsV1(data)

    def get_shop(self, language: str = 'en', render_data: str = 'false') -> ShopV2:
        """

        :param language: supported languages
        :param render_data: 'true' or 'false' if you want render data or not (Default 'false')
        :return: ShopV2 object
        """

        params = {'lang': language, 'renderData': f'{render_data}'}
        data = self.http.get('v2/shop', params=params)
        return ShopV2(data)

    def get_account_by_id(self, username: str) -> dict:
        """

        :param username:
        :return:
        """

        params = {'username': username}
        data = self.http.get('v1/lookup', params=params)
        return data

    def get_account_stats(self, account_id: str) -> dict:
        """

        :param account_id:
        :return:
        """

        params = {'account': account_id}
        data = self.http.get('v1/stats', params=params)
        return data

    def get_recent_matches(self, account_id: str) -> dict:
        """

        :param account_id:
        :return:
        """

        params = {'account': account_id}
        data = self.http.get('v1/matches', params=params)
        return data

    def get_news(self, language: str = 'en', news_type: str = None) -> dict:
        """

        :param language:
        :param news_type:
        :return:
        """

        params = {'lang': language}
        if news_type:
            params['type'] = news_type

        data = self.http.get('v1/news', params=params)
        return data

    def get_battle_pass_reward(self) -> None:
        pass

    def get_achievements(self, language: str = 'en') -> AchievementsV1:
        """
        Get all achievements

        :param language: supported languages
        :return: AchievementsV1 object
        """

        params = {'lang': language}
        data = self.http.get('v1/achievements', params=params)
        return AchievementsV1(data)

    def get_tournaments(self) -> None:
        pass

    def get_tournament_details(self) -> None:
        pass

    def get_tournament_scores(self) -> None:
        pass

    def get_map(self) -> None:
        pass

    def get_map_list(self) -> None:
        pass

    def get_loot_list(self, language: str = 'en') -> LootListV1:
        """
        Get current in-game loot

        :param language: supported languages
        :return: LootListV1 object
        """

        params = {'lang': language}
        data = self.http.get('v1/loot/list', params=params)
        return LootListV1(data)
