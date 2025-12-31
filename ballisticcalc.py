from py_ballisticcalc import *

# Changing to metric units to match Tarkov
PreferredUnits.distance = Distance.Meter
PreferredUnits.adjustment = Angular.Mil





# Setting a ammo type for 5.56 FMJ. This will hopefully be done with an API in the future.
# 
fmj = Ammo(
    dm=DragModel(0.252, TableG1),
    mv=Unit.MPS(904.6)
)

# Creating the adar as a weapon to insert the sight height
adar = Weapon(sight_height=Unit.Millimeter(68.58))

# Setting the zero distance to 200 meters with shot
zero_distance = Distance.Meter(200)
calc = Calculator()
shot = Shot(weapon=adar, ammo=fmj)
zero_elev = calc.set_weapon_zero(shot, zero_distance)


# Creating the shot distance required and running the "fire" calculation"
shot_distance = Distance.Meter(500)
hit = calc.fire(shot, trajectory_range=shot_distance, trajectory_step=Distance.Meter(10))
adjustment = hit.get_at("slant_distance", shot_distance)

# Printing the final result
print(f"Hold at {shot_distance}m: {adjustment.drop_angle << Angular.Mil}")


# Will want to make a function that accepts these parameters: sight height, velocity, BC, zero, and distance,
# and return an estimated mil drop for these