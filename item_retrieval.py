import json
from pathlib import Path
from dataclasses import dataclass
# importing initial libraries



# Creating an AmmoItem class for the needed parameters
@dataclass(frozen=True)
class AmmoItem:
    key: str
    id: str
    caliber: str
    velocity: float
    bc: float

# Creating a WeaponItem class as the default ammunition type is needed
@dataclass(frozen=True)
class WeaponItem:
    key: str
    id: str
    default_load_id: str

# Creating an initial value to store the ammo list under
AMMO_REGISTRY = None

def load_registries(path: str):

    # checking to see if the json has already been read
    global AMMO_REGISTRY 
    if AMMO_REGISTRY != None: return

    # opening the items.json file
    with open(path, "r", encoding = "utf-8") as f:
        raw = json.load(f)

    # Creating the registry for both weapons and ammunition
    ammo_registry = {}
    weapon_registry = {}

    for item in raw.values(): # For each item in the json
        properties = item.get("_props")
        item_id = item.get("_id")

        name = item.get("_name")
        properties = item.get("_props")

        # Making sure that this is a valid item
        if not name or not properties: continue

        # Checking to see if the item is ammunition
        if "ammoType" in properties:
            ammo_registry[name] = AmmoItem(
                key = name,
                id = item_id,
                caliber = properties["Caliber"],
                velocity = properties["InitialSpeed"],
                bc = properties["BallisticCoeficient"]
                )
            continue

        # Checking to see if the item is a weapon
        if "defAmmo" in properties:
            weapon_registry[name] = WeaponItem(
                key = name,
                id = item_id,
                default_load_id = properties["defAmmo"]
            )


    return ammo_registry, weapon_registry


def find_ammo_by_caliber(caliber: str) -> list[str]:
    return [ name for name, props in AMMO_REGISTRY.items() if props.get("Caliber") == caliber]


def list_ammo_names() -> list[str]:
    return sorted(AMMO_REGISTRY.keys())