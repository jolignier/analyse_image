# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdditionSubstractionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AdditionSubstractionDialog(QDialog):

    def __init__(self, liste, *args, **kwargs):
        super(AdditionSubstractionDialog, self).__init__(*args, **kwargs)

        self.liste = liste

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
        self.radio_addition = QRadioButton(self.groupBox_2)
        self.radio_addition.setObjectName("radio_addition")
        self.horizontalLayout_2.addWidget(self.radio_addition)
        self.radio_substract = QRadioButton(self.groupBox_2)
        self.radio_substract.setObjectName("radio_substract")
        self.horizontalLayout_2.addWidget(self.radio_substract)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)
        self.image1_choice = QComboBox(self.groupBox_2)
        self.image1_choice.setObjectName("image1_choice")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.image1_choice)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)
        self.image2_choice = QComboBox(self.groupBox_2)
        self.image2_choice.setObjectName("image2_choice")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.image2_choice)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(2, QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(0, QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(4, QFormLayout.FieldRole, spacerItem2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QMetaObject.connectSlotsByName(self)

        self.fillChoiceBox()
        self.radio_addition.setEnabled(False)
        self.radio_substract.setEnabled(False)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Options"))
        self.groupBox_2.setTitle(_translate("Dialog", "Options d\'entrées"))
        self.label_2.setText(_translate("Dialog", "Type :"))
        self.radio_addition.setText(_translate("Dialog", "Addition"))
        self.radio_substract.setText(_translate("Dialog", "Soustraction"))
        self.label.setText(_translate("Dialog", "Image 1 :"))
        self.label_3.setText(_translate("Dialog", "Image 2 :"))

    def fillChoiceBox(self):
        for elt in self.liste:
            title = elt.windowTitle()
            self.image1_choice.addItem(title);
            self.image2_choice.addItem(title);

    def getTitles(self):
        title1 = self.image1_choice.currentText()
        title2 = self.image2_choice.currentText()
        return title1, title2