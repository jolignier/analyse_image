from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np


##########################################################
##########################################################

# Idea to implement:
# We are strongly familiair with numpy array and not Qt
# And basically we can considerate images as np array
# convert
# --> Apply treatment to images as np array
# --> Transform the np array to QPixmap
# --> Return the QPixmap

##########################################################
##########################################################

# Si le pixel est supérieur au seuil,
# celui ci est blanc
def seuillage_haut(image: QImage, seuil: int):
    new_image = image

    for i in range(0, image.width()):
        for j in range(0, image.height()):
            if image.pixel(i, j) > qRgb(seuil, seuil, seuil):
                new_image.setPixel(i, j, qRgb(255,255,255))
    return new_image

# Si le pixel est inférieur au seuil,
# celui ci est noir
def seuillage_bas(image: QImage, seuil: int):
    new_image = image

    for i in range(0, image.width()):
        for j in range(0, image.height()):
            if image.pixel(i, j) < qRgb(seuil, seuil, seuil):
                new_image.setPixel(i, j, qRgb(0,0,0))
    return new_image


def addition(image1, image2):
    print("TODO")
    return 0;


def soustraction(image1, image2):
    print("TODO")
    return 0;


def erosion(image, strel):
    print("TODO")
    return 0;


def dilatation(image, strel):
    print("TODO")
    return 0;


def ouverture(image, strel):
    print("TODO")
    return 0;


def fermeture(image, strel):
    print("TODO")
    return 0;


def amincissement(image, strel):
    print("TODO")
    return 0;


def epaississement(image, strel):
    print("TODO")
    return 0;


def squelettisation_Lantuejoul(image):
    print("TODO")
    return 0;


def squelettisation_amincissement_homothopique(image):
    print("TODO")
    return 0;


