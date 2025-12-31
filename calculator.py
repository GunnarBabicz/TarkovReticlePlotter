from py_ballisticcalc import *



# given these parameters, the adjustment in mils required for the round is provided
def calculate_drop(sight_height: float, muzzle_velocity: float, coefficient: float, zero_distance: int, shot_distance: float):
    # Changing to metric units to match Tarkov
    PreferredUnits.distance = Distance.Meter
    PreferredUnits.adjustment = Angular.Mil

    #Setting units
    sight_height = Distance.Millimeter(sight_height)
    muzzle_velocity = Unit.MPS(muzzle_velocity)
    zero_distance = Unit.Meter(zero_distance)
    shot_distance = Unit.Meter(shot_distance)

    # Setting a ammo type for 5.56 FMJ. This will hopefully be done with an API in the future.
    # 
    used_ammo = Ammo(
        dm=DragModel(coefficient, TableG1),
        mv=muzzle_velocity
    )

    # Creating the adar as a weapon to insert the sight height
    used_weapon = Weapon(sight_height=sight_height)

    # Setting the zero distance to 200 meters with shot
    calc = Calculator()
    shot = Shot(weapon=used_weapon, ammo=used_ammo)
    calc.set_weapon_zero(shot, zero_distance)

    # Setting the trajectory range an extra step so there are points on both sides to calculate
    step = Distance.Meter(10)
    trajectory_range = shot_distance + step


    # Creating the shot distance required and running the "fire" calculation"
    hit = calc.fire(shot, trajectory_range=trajectory_range, trajectory_step=Distance.Meter(10), dense_output=True)
    adjustment = hit.get_at("slant_distance", shot_distance)

    # Printing the raw result for testing purposes
    print(f"Hold at {shot_distance}: {adjustment.drop_angle << Angular.Mil}")



# ballistic coefficient = 0.252
# velocity = 904.6
# sight height = 68.58
# zero distance = 200


calculate_drop(68.58, 904.6, 0.252, 200, 100)


