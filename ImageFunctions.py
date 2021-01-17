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
    new_image = image

    for i in range(len(strel) / 2, image.width - len(strel) / 2):
        for j in range(len(strel) / 2, image.height - len(strel) / 2):



            for k in range(i - len(strel) / 2, i + len(strel) / 2):
                for l in range(j - len(strel) / 2, j + len(strel) / 2):

                    if QColor(image.pixel(k, l)).getRgb()[0] == 0:
                        new_image.setPixel(i, j, qRgb(0, 0, 0))
                        break

                if QColor(image.pixel(k, l)).getRgb()[0] == 0:
                    break

    return new_image;


def dilatation(image, strel) -> QImage:
    new_image = image

    for i in range(len(strel) / 2, image.width - len(strel) / 2):
        for j in range(len(strel) / 2, image.height - len(strel) / 2):


            for k in range(i - len(strel) / 2, i + len(strel) / 2):
                for l in range(j - len(strel) / 2, j + len(strel) / 2):

                    if QColor(image.pixel(k, l)).getRgb()[0] == 255:
                        new_image.setPixel(i, j, qRgb(255, 255, 255))
                        break

                if QColor(image.pixel(k, l)).getRgb()[0] == 255:
                    break

    return new_image;


def ouverture(image, strel) -> QImage:
    print("TODO")
    return 0;


def fermeture(image, strel) -> QImage:
    print("TODO")
    return 0;


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
