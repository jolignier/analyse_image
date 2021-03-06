# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view\ErosionDilatationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SquelettisationDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(SquelettisationDialog, self).__init__(*args, **kwargs)

        self.setObjectName("Dialog")
        self.resize(403, 309)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QGroupBox(self)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.radio_thinning = QRadioButton(self.groupBox)
        self.radio_thinning.setObjectName("radio_thinning")
        self.horizontalLayout_3.addWidget(self.radio_thinning)
        self.radio_lantuejoul = QRadioButton(self.groupBox)
        self.radio_lantuejoul.setObjectName("radio_lantuejoul")
        self.horizontalLayout_3.addWidget(self.radio_lantuejoul)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addWidget(self.groupBox_2)
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

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Options"))
        self.label_4.setText(_translate("Dialog", "Type d\'opération :"))
        self.radio_thinning.setText(_translate("Dialog", "Amincissement Homotopique"))
        self.radio_lantuejoul.setText(_translate("Dialog", "Lantuéjoul"))
        self.groupBox_2.setTitle(_translate("Dialog", "Options d\'entrées"))

    def getValues(self):
        return self.radio_thinning.isChecked()
