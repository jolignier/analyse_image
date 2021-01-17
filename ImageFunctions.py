from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import numpy as np
import math


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

def binarisation(image: QImage, seuil):
    new_image = seuillage_haut(image, seuil)
    final_image = seuillage_bas(new_image, seuil)
    return final_image


# Si le pixel est supérieur au seuil,
# celui ci est blanc
def seuillage_haut(image: QImage, seuil: int) -> QImage:
    new_image = image

    for i in range(0, image.width()):
        for j in range(0, image.height()):
            if image.pixel(i, j) >= qRgb(seuil, seuil, seuil):
                new_image.setPixel(i, j, qRgb(255,255,255))
    return new_image


# Si le pixel est inférieur au seuil,
# celui ci est noir
def seuillage_bas(image: QImage, seuil: int) -> QImage:
    new_image = image

    for i in range(0, image.width()):
        for j in range(0, image.height()):
            if image.pixel(i, j) < qRgb(seuil, seuil, seuil):
                new_image.setPixel(i, j, qRgb(0, 0, 0))
    return new_image


def addition(image1, image2) -> QImage:
    new_image = image1

    for i in range(0, image1.width()):
        for j in range(0, image1.height()):
            pixel1 = QColor(image1.pixel(i, j)).getRgb()
            pixel2 = QColor(image2.pixel(i, j)).getRgb()
            r = pixel1[0] + pixel2[0] if pixel1[0] + pixel2[0] < 255 else 255
            g = pixel1[1] + pixel2[1] if pixel1[1] + pixel2[1] < 255 else 255
            b = pixel1[2] + pixel2[2] if pixel1[2] + pixel2[2] < 255 else 255
            new_image.setPixel(i, j, qRgb(r, g, b))
    return new_image


def soustraction(image1: QImage, image2) -> QImage:
    new_image = image1

    for i in range(0, image1.width()):
        for j in range(0, image1.height()):
            pixel1 = QColor(image1.pixel(i, j)).getRgb()
            pixel2 = QColor(image2.pixel(i, j)).getRgb()
            r = pixel1[0] - pixel2[0] if pixel1[0] + pixel2[0] > 0 else 0
            g = pixel1[1] - pixel2[1] if pixel1[1] + pixel2[1] > 0 else 0
            b = pixel1[2] - pixel2[2] if pixel1[2] + pixel2[2] > 0 else 0
            new_image.setPixel(i, j, qRgb(r, g, b))
    return new_image


def erosion(image: QImage, strel: list) -> QImage:
    new_image = QImage(image)
    half_strel = math.floor(len(strel)/2)
    last_pixel = 0
    isInObject = False
    for i in range(half_strel, image.width()-half_strel):
        for j in range(half_strel, image.height()-half_strel):
            # if transition = change betwen outside and inside
            if QColor(image.pixel(i, j)).getRgb()[0] != last_pixel:
                isInObject = False if isInObject else True

            if isInObject:
                hasBlackPixel = False
                for k in range(i - half_strel, i + half_strel):
                    for l in range(j - half_strel, j + half_strel):
                        if QColor(image.pixel(k, l)).getRgb()[0] == 0:
                            hasBlackPixel = True
                            break
                    if hasBlackPixel:
                        break
                if hasBlackPixel:
                    for k in range(i - half_strel, i + half_strel):
                        for l in range(j - half_strel, j + half_strel):
                            new_image.setPixel(k, l, qRgb(0, 0, 0))




    return new_image


def dilatation(image, strel) -> QImage:
    new_image = QImage(image)
    half_strel = math.floor(len(strel)/2)
    for i in range(half_strel, image.width()-half_strel, len(strel)-1):
        for j in range(half_strel, image.height()-half_strel, len(strel)-1):
            # Strel
            hasWhitePixel = False
            for k in range(i - half_strel, i + half_strel):
                for l in range(j - half_strel, j + half_strel):
                    if  QColor(image.pixel(k, l)).getRgb()[0] == 255:
                        hasWhitePixel = True
                        break
            if hasWhitePixel:
                for k in range(i - half_strel, i + half_strel):
                    for l in range(j - half_strel, j + half_strel):
                        new_image.setPixel(k, l, qRgb(255,255,255))

    return new_image


def ouverture(image, strel) -> QImage:
    new_image = erosion(dilatation(image, strel), strel)
    return new_image

def fermeture(image, strel) -> QImage:
    new_image = dilatation(erosion(image, strel), strel)
    return new_image

def amincissement(image, strel) -> QImage:
    print("TODO")
    return 0;


def epaississement(image, strel) -> QImage:
    print("TODO")
    return 0;


def squelettisation_Lantuejoul(image) -> QImage:
    print("TODO")
    return 0;


def squelettisation_amincissement_homothopique(image) -> QImage:
    print("TODO")
    return 0;


def createStrel(dim, isBoule=False):
    strel = []
    line = [255] * dim
    for i in range(0, dim):
        strel.append(line)

    return strel
