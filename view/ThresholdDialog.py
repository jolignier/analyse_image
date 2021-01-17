# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ThresholdDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ImageFunctions
import time

class ThresholdDialog(QDialog):


    def __init__(self, image, *args, **kwargs):
        super(ThresholdDialog, self).__init__(*args, **kwargs)

        self.image = image
        self.new_image = QImage()

        self.setObjectName("Dialog")
        self.resize(403, 309)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QGroupBox(self)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.radio_high = QRadioButton(self.groupBox_2)
        self.radio_high.setObjectName("radio_high")
        self.radio_high.setChecked(True)
        self.horizontalLayout_2.addWidget(self.radio_high)
        self.radio_low = QRadioButton(self.groupBox_2)
        self.radio_low.setObjectName("radio_low")
        self.horizontalLayout_2.addWidget(self.radio_low)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.slider = QSlider(self.groupBox_2)
        self.slider.setAutoFillBackground(False)
        self.slider.setMaximum(255)
        self.slider.setSliderPosition(127)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.horizontalLayout_3.addWidget(self.slider)
        self.slider_value = QLabel(self.groupBox_2)
        self.slider_value.setObjectName("slider_value")
        self.horizontalLayout_3.addWidget(self.slider_value)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.preview = QLabel(self.groupBox_3)
        self.preview.setMinimumSize(QSize(128, 128))
        self.preview.setText("")
        self.preview.setObjectName("preview")
        self.preview.setScaledContents(True)

        self.preview_button = QPushButton(self.groupBox_3)
        self.preview_button.setText("Mettre à jour l'apercu")
        self.preview_button.setObjectName("preview_button")

        self.verticalLayout_3.addWidget(self.preview)
        self.verticalLayout_3.addWidget(self.preview_button)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.slider.valueChanged['int'].connect(self.slider_value.setNum)
        self.preview_button.pressed.connect(self.actualizePreview)
        QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Options de Seuillage"))
        self.groupBox_2.setTitle(_translate("Dialog", "Options de seuillage"))
        self.label_2.setText(_translate("Dialog", "Type de seuillage :"))
        self.radio_high.setText(_translate("Dialog", "Haut"))
        self.radio_low.setText(_translate("Dialog", "Bas"))
        self.label.setText(_translate("Dialog", "Seuil (0-255) :"))
        self.slider_value.setText(_translate("Dialog", "127"))
        self.groupBox_3.setTitle(_translate("Dialog", "Aperçu de l\'image"))


    def getImage(self) -> QImage:
        return self.new_image


    def actualizePreview(self):
        seuillage_haut = self.radio_high.isChecked()
        seuil = self.slider.value()
        # Avoid image and new_image to become the same object (same adress)
        temp = QImage(self.image)
        if seuillage_haut:
            self.new_image = ImageFunctions.seuillage_haut(temp, seuil)
        else:
            self.new_image = ImageFunctions.seuillage_bas(temp, seuil)
        self.preview.setPixmap(QPixmap(self.new_image).scaled(self.preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))