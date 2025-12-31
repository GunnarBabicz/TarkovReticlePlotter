# Create a class for scope characteristics
# Will need to create directory for reticle photos
import numpy 
import cv2


class scope():
    def __init__(self, name, cmPer100Meter, pixelsBetweenMils, imageDirectory) -> None:
        self.name = name
        self.cmPer100Meter = cmPer100Meter
        self.pixelsBetweenMils = pixelsBetweenMils # This is already adjusted with the cmPer100Meter Adjustment
        self.imageDirectory = imageDirectory


Valday = scope("PS-320 Valday", 12.1, 12.39669421487603, "Scopes/Valday/Valday_PS-320_reticle.png")
