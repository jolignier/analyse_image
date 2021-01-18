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

def amincissement(image, strel, max_iter) -> QImage:
    new_image = QImage(image)
    # Half strel is always 3/2 => 1
    for nb_iter in range(0, max_iter*8):
        new_image = QImage(image)
        for i in range(1, image.width() - 1):
            for j in range(1, image.height() - 1):
                #Strel
                if doStrelFit(image, i, j, strel):
                    new_image.setPixel(i, j, qRgb(0, 0, 0))
        strel = getNextStrel(strel)
        print("FINISHED ITERATION ", nb_iter)
        image = QImage(new_image)
    return new_image



def epaississement(image, strel, max_iter) -> QImage:
    new_image = QImage(image)
    # Half strel is always 3/2 => 1
    for nb_iter in range(0, max_iter * 8):
        new_image = QImage(image)
        for i in range(1, image.width() - 1):
            for j in range(1, image.height() - 1):
                # Strel
                if doStrelFit(image, i, j, strel):
                    new_image.setPixel(i, j, qRgb(255, 255, 255))
        strel = getNextStrel(strel)
        print("FINISHED ITERATION ", nb_iter)
        image = QImage(new_image)
    return new_image


def squelettisation_Lantuejoul(image) -> QImage:
    height, width = image.shape

    resultat = np.zeros((height, width), dtype=np.uint8)

    stop = 1
    compteur = 0
    degre_erosion = 0
    while stop != 0:
        img1 = image.copy()
        compteur = 0

        # VERIFICATION SI IMAGE NOIR (vide)
        for degre in range(0, degre_erosion):
            img1 = erosion(img1)

        for i in range(0, height):
            for j in range(0, width):
                val1 = int(img1[i, j])
                if val1 == 255:
                    compteur = compteur + 1
        stop = compteur
        img2 = ouverture(img1)

        img3 = soustraction(img1, img2)

        resultat = addition(resultat, img3)
        degre_erosion = degre_erosion + 1

    # Lantuejoul Resultat_n = Resultat_n-1 + (erosion - ouverture)


def squelettisation_amincissement_homothopique(image) -> QImage:
    strel = createThinningStrel()
    new_image = amincissement(image, strel, 1)
    while image != new_image:
        image = new_image
        new_image = amincissement(new_image, strel, 1)
    return new_image

def doStrelFit(image,i,j, strel):
    nb_fit = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if QColor(image.pixel(i - k, j - l)).getRgb()[0] == strel[k + 1][l + 1] or strel[k + 1][l + 1] == 111:
                nb_fit +=1
    if nb_fit == 9:
        return True
    else:
        return False

def createStrel(dim, isBoule=False):
    strel = []
    line = [255] * dim
    for i in range(0, dim):
        strel.append(line)

    return strel

def createThinningStrel():
    return [
        [0, 0, 0],
        [111, 255, 111 ], # 111 is the joker v
        [255, 255, 255]
    ]

def createThickingStrel():
    return [
        [0, 0, 0],
        [111, 0, 111 ], # 111 is the joker v
        [255, 255, 255]
    ]

def getNextStrel(s):
    return [
        [ s[1][0], s[0][0], s[0][1] ],
        [ s[2][0], s[1][1], s[0][2] ],
        [ s[2][1], s[2][2], s[1][2] ]
    ]