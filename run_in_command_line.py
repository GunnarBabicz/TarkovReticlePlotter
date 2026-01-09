import ammo_library

# Creating the ammo library that will be needed for looking up by item name
ammoLibrary = ammo_library.load_ammo_registry("items.json")

# Looking up the ammo by the string that has been assigned to it
print(ammoLibrary["patron_556x45_M855"].bc)




"""

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