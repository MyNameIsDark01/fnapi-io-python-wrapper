import fnapi_io
import json

api = fnapi_io.FortniteApi(api_key='')
challenge = api.get_challenges()
open('tests/test_challenge.json', 'w+').write(json.dumps(challenge, default=lambda o: o.__dict__, indent=4))
items = api.get_upcoming_items()
open('tests/test_upcoming.json', 'w+').write(json.dumps(items, default=lambda o: o.__dict__, indent=4))
item_detail = api.get_item_details(item_id='CID_242_Athena_Commando_F_Bullseye')
open('tests/test_details.json', 'w+').write(json.dumps(item_detail, default=lambda o: o.__dict__, indent=4))
shop = api.get_shop(render_data='true')
open('tests/test_shop.json', 'w+').write(json.dumps(shop, default=lambda o: o.__dict__, indent=4))
loot = api.get_loot_list()
open('tests/test_loot.json', 'w+').write(json.dumps(loot, default=lambda o: o.__dict__, indent=4))
achievement = api.get_achievements()
open('tests/test_achievements.json', 'w+').write(json.dumps(achievement, default=lambda o: o.__dict__, indent=4))
sets = api.get_list_of_sets()
open('tests/test_sets.json', 'w+').write(json.dumps(sets, default=lambda o: o.__dict__, indent=4))
