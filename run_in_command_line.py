import item_retrieval

# Creating the ammo library that will be needed for looking up by item name
ammo_library, weapon_library = item_retrieval.load_registries("items.json")


selected_ammo = ammo_library["patron_556x45_55_FMJ"]
selected_weapon = weapon_library["weapon_adar_2-15_556x45"]
# Looking up the ammo by the string that has been assigned to it
print(selected_ammo)
print(selected_weapon)


# This will determine whether or not the ammo being chosen 
# is the default load for a weapon. This can be used to either run a
# default calculation, or a slightly modified one based on the parameters

print(selected_ammo.id == selected_weapon.default_load_id)





"""
ammo names for testing: "patron_556x45_M855", "patron_556x45_55_FMJ"


We will want to make a separate command line item to be able to collect the parameters that will be required for the program.

Here are some of the following items we will need:


REQUIRED:
Muzzle Velocity
Ballistic Coefficient 
sight zero
max range
number of desired intervals (This can be anything from 1 to 10)
sight height (default number will be suggested)

OPTIONAL:

Tag (This could be used to mark ammo type, velocity, etc.)



"""