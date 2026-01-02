from py_ballisticcalc import *



# given these parameters, the adjustment in mils required for the round is provided
def calculate_mil_adjustments(sight_height: float, muzzle_velocity: float, coefficient: float, zero_distance: int, distances: list[float]):
    # Changing to metric units to match Tarkov
    PreferredUnits.distance = Distance.Meter
    PreferredUnits.adjustment = Angular.Mil

    #Setting units
    sight_height = Unit.Millimeter(sight_height)
    muzzle_velocity = Unit.MPS(muzzle_velocity)
    zero_distance = Distance.Meter(zero_distance)
    max_distance = Distance.Meter(max(distances))

    # Setting a ammo type for 5.56 FMJ. This will hopefully be done with an API in the future.
    # 
    used_ammo = Ammo(
        dm=DragModel(coefficient, TableG1),
        mv=muzzle_velocity
    )

    # Creating the weapon to insert the sight height
    used_weapon = Weapon(sight_height=sight_height)


    # Setting the zero distance to 200 meters with shot
    calc = Calculator()
    shot = Shot(weapon=used_weapon, ammo=used_ammo)
    calc.set_weapon_zero(shot, zero_distance)

    # Setting the trajectory range an extra step so there are points on both sides to calculate
    step = Distance.Meter(10)
    trajectory_range = max_distance + step


    # Creating the shot distance required and running the "fire" calculation"
    hit = calc.fire(shot, trajectory_range=trajectory_range, trajectory_step=Distance.Meter(10), dense_output=True)


    # Creating a dictionary for the adjustments at each range
    adjustment_dictionary: dict[float, float] = {}

    for i in distances:
        # Calculating the adjustment needed at this distance
        distance = Distance.Meter(i)
        adjustment = hit.get_at("slant_distance", distance)

        # Adjusting to a float with string replacement
        mils = float(str(adjustment.drop_angle << Angular.Mil).replace("mil", ""))

        # Adding to the dictionary
        adjustment_dictionary[i] = (mils)
    # Printing the raw result for testing purposes
    return adjustment_dictionary



# values for testing purposes
# ballistic coefficient = 0.252
# velocity = 904.6
# sight height = 68.58
# zero distance = 200

#distances = [50,100,150,200,250,300,350,400,450,500]

#test = calculate_mil_adjustments(68.58, 904.6, 0.252, 200, distances)

#print(test)




