import requests


def spell_requester(spell_name: str):
    spell_name = spell_name.replace(" ", "-")
    spell_name = spell_name.lower()

    response = requests.get(f"https://www.dnd5eapi.co/api/spells/{spell_name}")

    json_dict = response.json()
    damage = next(iter(json_dict["damage"]["damage_at_slot_level"].values()))
    return damage


pass
