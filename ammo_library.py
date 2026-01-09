import json
from pathlib import Path
from dataclasses import dataclass
# importing initial libraries



@dataclass(frozen=True)
class Ammo:
    key: str
    caliber: str
    velocity: float
    bc: float

# Creating an initial value to store the ammo list under
AMMO_REGISTRY = None

def load_ammo_registry(path: str) -> dict[str, Ammo]:

    # checking to see if the json has already been read
    global AMMO_REGISTRY 
    if AMMO_REGISTRY != None: return

    # opening the items.json file
    with open(path, "r", encoding = "utf-8") as f:
        raw = json.load(f)

    registry = {}

    for item in raw.values(): # For each item in the json
        properties = item.get("_props")

        name = item.get("_name")
        properties = item.get("_props")

        # Making sure that this is a valid item
        if not name or not properties: continue

        # Checking to see if the item is ammunition
        if "ammoType" not in properties: continue

        registry[name] = Ammo(
            key = name,
            caliber = properties["Caliber"],
            velocity = properties["InitialSpeed"],
            bc = properties["BallisticCoeficient"]
            )

    return registry


def find_ammo_by_caliber(caliber: str) -> list[str]:
    return [ name for name, props in AMMO_REGISTRY.items() if props.get("Caliber") == caliber]


def list_ammo_names() -> list[str]:
    return sorted(AMMO_REGISTRY.keys())