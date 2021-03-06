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
    new_image = QImage(image)

    for i in range(0, image.width()):
        for j in range(0, image.height()):
            if image.pixel(i, j) >= qRgb(seuil, seuil, seuil):
                new_image.setPixel(i, j, qRgb(255,255,255))
    return new_image


# Si le pixel est inférieur au seuil,
# celui ci est noir
def seuillage_bas(image: QImage, seuil: int) -> QImage:
    new_image = QImage(image)

    for i in range(0, image.width()):
        for j in range(0, image.height()):
            if image.pixel(i, j) < qRgb(seuil, seuil, seuil):
                new_image.setPixel(i, j, qRgb(0, 0, 0))
    return new_image


def addition(image1, image2) -> QImage:
    new_image = QImage(image1)

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
    new_image = QImage(image1)

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
    new_image.fill(Qt.black)
    half_strel = math.floor(len(strel)/2)

    for i in range(half_strel, image.width()-half_strel):
        for j in range(half_strel, image.height()-half_strel):
            if QColor(image.pixel(i, j)).getRgb()[0] == 255:
                doFit = True
                for k in range(-half_strel, half_strel + 1):
                    for l in range(-half_strel, half_strel + 1):
                        if (strel[k][l]==255 and QColor(image.pixel(i+k, l+j)).getRgb()[0] != strel[k][l]):
                            doFit = False
                if doFit:
                    new_image.setPixel(k+i, l+j, qRgb(255, 255, 255))

    return new_image


def dilatation(image, strel) -> QImage:

    new_image = QImage(image)
    new_image.fill(Qt.black)
    half_strel = math.floor(len(strel) / 2)

    for i in range(half_strel, image.width()-half_strel+1):
        for j in range(half_strel, image.height()-half_strel+1):
            # Strel
            hasWhitePixel = False
            for k in range(i - half_strel, i + half_strel+1):
                for l in range(j - half_strel, j + half_strel+1):
                    if QColor(image.pixel(k, l)).getRgb()[0] == 255:
                        hasWhitePixel = True
                        break
            if hasWhitePixel:
                for k in range(- half_strel, half_strel+1):
                    for l in range( - half_strel, half_strel+1):
                        if strel[k][l] == 255:
                            new_image.setPixel(i+k, j+l, qRgb(255, 255, 255))

    return new_image


def ouverture(image, strel) -> QImage:
    dilatee = dilatation(image, strel)
    new_image = erosion(dilatee, strel)
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
    resultat = QImage(image)
    resultat.fill(Qt.black)

    stop = 1
    rayon = 1
    open_strel = createBall(3)

    while stop != 0:
        img1 = QImage(image)
        compteur = 0
        strel = createBall(rayon*2 +1)

        img1 = erosion(img1, strel)

        for i in range(0, img1.width()):
            for j in range(0, img1.height()):
                if QColor(img1.pixel(i, j)).getRgb()[0] == 255:
                    compteur += 1

        stop = compteur
        img2 = ouverture(img1, open_strel)
        img3 = soustraction(img1, img2)
        resultat = addition(resultat, img3)

        print(compteur)
        rayon += 1

        # U [(X ⊖ kB)] − [(X ⊖ kB) ◦ B]
        # SOMME DES erosion(img, boule taille k) - ouverture(erodée)
    return resultat


def squelettisation_amincissement_homothopique(image) -> QImage:
    strel = createThinningStrel()
    new_image = amincissement(image, strel, 1)
    while image != new_image:
        image = new_image
        new_image = amincissement(new_image, strel, 1)
    return new_image

def doStrelFit(image,i,j, strel):
    nb_fit = 0
    nb_whites = 0
    half_strel = math.floor(len(strel)/2)
    for k in range(-half_strel, half_strel+1):
        for l in range(-half_strel, half_strel+1):
            if QColor(image.pixel(i - k, j - l)).getRgb()[0] == strel[k + 1][l + 1] or strel[k + 1][l + 1] == 111:
                nb_fit +=1
    if nb_fit == 9:
        return True
    else:
        return False

def createStrel(dim, isBoule=False):
    if isBoule:
        return createBall(dim)
    strel = []
    line = [255] * dim
    for i in range(0, dim):
        strel.append(line)
    return strel

def createBall(diam):
    radius = math.floor(diam/2)
    a, b = radius, radius
    n = 2*radius +1

    y, x = np.ogrid[-a:n - a, -b:n - b]
    mask = x * x + y * y <= radius*radius

    array = np.zeros((n, n))
    array[mask] = 255


    res = []
    for i in range(0, n):
        line=[]
        for j in range(0, n):
            if array[i][j] < 50:
                line.append(0)
            else:
                line.append(255)
        res.append(line)

    return res

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