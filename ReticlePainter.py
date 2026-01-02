import cv2
import numpy as np
import scope
import calculator

# selects the scope being used from the library of entered scopes
scopeUsed = scope.Valday


# sets local parameters according to selected scope
cmRatio = scopeUsed.cmPer100Meter
pixelsPerMil = scopeUsed.pixelsBetweenMils
image = cv2.imread(scopeUsed.imageDirectory)




def annotatePlot(pixel, distance, i):
    """Adds the distance marking to the reticle"""
    font = cv2.FONT_HERSHEY_PLAIN
    fontScale = 0.6
    color = (255,0,0)
    thickness = 1
    if i % 2 == 0:
        org = (460, pixel)
        cv2.line(image, (498,pixel), (480, pixel), color, thickness)
    else:
        org = (525, pixel)
        cv2.line(image, (501,pixel), (520, pixel), color, thickness)
    
    cv2.putText(image, str(distance), org, font, fontScale, color, thickness, cv2.LINE_AA)
    


def addDescription(distance):
    """Describes the scope and weapon parameters"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.3
    color = (255,0,0)
    thickness = 1
    # Collects the scope/weapon parameters into a stack
    descList = []
    descList.append(("Scope: " + scopeUsed.name))
    descList.append(("Zero distance: " + str(distance) + "m"))
    # descList.append((f"Ammunition: {ammunition.caliber} {ammunition.loading}"))
    textHeight = 600

    # Writes the parameters in the corner of the reticle
    for i in descList:
        cv2.putText(image, i, (600,textHeight), font, 0.4, color, thickness, cv2.LINE_AA)
        textHeight = textHeight+20


def plotOnReticle(distance, drop, i, selectedScope):
    if abs(drop) != 0.00:

        pixel = 499 - round(drop * selectedScope.pixelsBetweenMils)

        #Step 4: Plot the point on the reticle
        if pixel > 950 or pixel < 50: # If the pixel is beyond the bounds of the optic
             return
        annotatePlot(pixel, distance, i)
        return
    addDescription(distance) # If no adjustment is needed, this is the zero distance
    



def runProgram(adjustment_dictionary, selectedScope):
    for i, (distance, adjustment) in enumerate(adjustment_dictionary.items()):
        plotOnReticle(distance, adjustment, i, selectedScope)
    cv2.imwrite("result.png", image)



# Creating the objects for the program
#tableRanges = ranges.createRangeObjects()
# ammunition = ranges.createAmmoObject()
# increment: The distance between each value that is given by the calculator.




# values for testing purposes
# ballistic_coefficient = 0.252
# velocity = 904.6
# sight_height = 68.58
# zero_distance = 200
distanceRanges = [50,100,150,200,250,300,350,400,450,500]

adjustment_dictionary = calculator.calculate_mil_adjustments(68.58, 904.6, 0.252, 200, distanceRanges)





# running the program
runProgram(adjustment_dictionary, scope.Valday)


