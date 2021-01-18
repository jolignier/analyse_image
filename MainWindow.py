import sys
from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources

import ImageFunctions

#
# Required modules are :
#   - PyQT5
#   - PyQT5-stubs
#   - PyQT5-sip
#   - numpy

# Optional:
# - PyQt5Designer : GUI Designer to export python code
#       -> Open with terminal in venv : designer.exe
#       -> To export code : pyuic5 input.ui -o output.py
#       -> To export qrc resources pyrcc5 resource.qrc -o resource.py



##############################################################################
# MainWindow Class is a Multiple Document Interface allowing us to manage
# Multiple windows and in details multiple Images shown in the application
##############################################################################
from view.AdditionSubstractionDialog import AdditionSubstractionDialog
from view.ErosionDilatationDialog import ErosionDilatationDialog
from view.ThresholdDialog import ThresholdDialog
from view.OpeningClosingDialog import OpeningClosingDialog
from view.ThinningThickingDialog import ThinningThickingDialog
from view.SquelettisationDialog import SquelettisationDialog


class MainWindow(QMainWindow):

    _subWindowCounter = 0

    ######################################################
    # Constructor of the MainWindow
    ######################################################

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Analyse d'images")
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        self._createActions()
        self._createToolBars()
        self._connectActions()

        with open("stylesheet.qss") as ss:
            self.setStyleSheet(ss.read())

    def _createToolBars(self):
        # File toolbar
        fileToolBar = self.addToolBar("File")
        fileToolBar.setMovable(False)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addAction(self.saveAsAction)

        # Edit toolbar
        editToolBar = QToolBar("Edit", self)
        editToolBar.setMovable(False)
        self.addToolBar(editToolBar)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)

        # Functions Tool bar
        functionsToolBar = QToolBar("Functions", self)
        functionsToolBar.setMovable(False)
        self.addToolBar(functionsToolBar)
        functionsToolBar.addAction(self.thresholdAction)
        functionsToolBar.addAction(self.additionAction)
        functionsToolBar.addAction(self.substractAction)
        functionsToolBar.addAction(self.erosionDilatationAction)
        functionsToolBar.addAction(self.openingClosingAction)
        functionsToolBar.addAction(self.thinningThickingAction)
        functionsToolBar.addAction(self.squelettisationAction)

    def _createActions(self):
        # File actions
        self.openAction = QAction(QIcon(":file-open"), "&Open...")
        self.saveAction = QAction(QIcon(":file-save"), "&Save")
        self.saveAsAction = QAction(QIcon(":file-saveAs"), "&Save As...")
        self.exitAction = QAction("&Exit", self)
        # String-based key sequences
        self.openAction.setShortcut("Ctrl+O")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAsAction.setShortcut("Ctrl+Shift+S")
        # Help tips
        # Edit actions
        self.copyAction = QAction(QIcon(":edit-copy"), "&Copy")
        self.pasteAction = QAction(QIcon(":edit-paste"), "&Paste")
        self.cutAction = QAction(QIcon(":edit-cut"), "C&ut")
        # Standard key sequence
        self.copyAction.setShortcut(QKeySequence.Copy)
        self.pasteAction.setShortcut(QKeySequence.Paste)
        self.cutAction.setShortcut(QKeySequence.Cut)

        #Functions Action
        self.thresholdAction = QAction("Seuillage")
        self.additionAction = QAction("Addition")
        self.substractAction = QAction("Soustraction")
        self.erosionDilatationAction = QAction("Erosion / Dilatation")
        self.openingClosingAction = QAction("Ouverture / Fermeture")
        self.thinningThickingAction = QAction("Amincissement / Epaississeement")
        self.squelettisationAction = QAction("Squelletisation")

    def _connectActions(self):
        # Connect File actions
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.saveAsAction.triggered.connect(self.saveAsFile)
        self.exitAction.triggered.connect(self.close)

        # Connect Edit actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)

        # Connect Functions actions
        self.thresholdAction.triggered.connect(self.thresholdImage)
        self.additionAction.triggered.connect(self.additionImage)
        self.substractAction.triggered.connect(self.substractImage)
        self.erosionDilatationAction.triggered.connect(self.erosionDilatation)
        self.openingClosingAction.triggered.connect(self.openingClosing)
        self.thinningThickingAction.triggered.connect(self.thinningThicking)
        self.squelettisationAction.triggered.connect(self.squelettisation)

    def openFile(self):
        # Get file to load
        file = QFileDialog.getOpenFileName(self, 'Open File', '', "Image files (*.jpg *.gif *.png)")
        file_path = file[0]
        # create a subwindow with the image
        isOpen = False
        for sub in self.mdi.subWindowList():
            if sub.windowTitle() == file_path:
                isOpen = True
                self.mdi.setActiveSubWindow(sub)
                break;
        if not isOpen:
            pixmap = QPixmap(file_path)
            self.createMDISubWindow(file_path, pixmap, True)


    def saveFile(self):
        self.saveAsFile()


    def saveAsFile(self):
        selectedSubWindow = self.getFocusedSubWindow()
        if selectedSubWindow is not None:
            image = selectedSubWindow.widget().pixmap()
            fileName = QFileDialog.getSaveFileName(self, 'Sauvegarder sous ...', '', "Images Files (*.png *.jpeg *.gif)")[0]
            if not fileName == '':
                image.save(fileName, "PNG")

    def copyContent(self):
        # Logic for copying content goes here...
        print("TODO")

    def pasteContent(self):
        # Logic for pasting content goes here...
        print("TODO")

    def cutContent(self):
        # Logic for cutting content goes here...
        print("TODO")

    def createMDISubWindow(self, title, pixmap, isExistingImage=False):
        sub = QMdiSubWindow()
        label_image = QLabel()
        label_image.setPixmap(pixmap)
        label_image.setAlignment(Qt.AlignCenter)
        sub.setWindowTitle(title)
        sub.setWidget(label_image)
        sub.adjustSize()
        self.mdi.addSubWindow(sub)
        sub.show()
        if not isExistingImage:
            self._subWindowCounter +=1

    def thresholdImage(self):
        selectedSubWindow = self.getFocusedSubWindow()
        if selectedSubWindow is not None:
            image = selectedSubWindow.widget().pixmap().toImage()
            image = image.convertToFormat(QImage.Format_Grayscale8)
            dialog = ThresholdDialog(image)
            result = dialog.exec_()
            if result == QDialog.Accepted:
                self.createMDISubWindow("Sans Titre "+str(self._subWindowCounter), QPixmap(dialog.getImage()))

    def additionImage(self):
        liste = self.mdi.subWindowList()
        if len(liste) > 0:
            dialog = AdditionSubstractionDialog(liste)
            dialog.radio_addition.setChecked(True)
            dialog.radio_substract.setChecked(False)
            result = dialog.exec_()
            if result == QDialog.Accepted:
                title1, title2 = dialog.getTitles()
                for sub in liste:
                    if title1 == sub.windowTitle():
                        sub1 = sub
                    if title2 == sub.windowTitle():
                        sub2 = sub
                image1 = sub1.widget().pixmap().toImage()
                image1 = image1.convertToFormat(QImage.Format_Grayscale8)
                image2 = sub2.widget().pixmap().toImage()
                image2 = image2.convertToFormat(QImage.Format_Grayscale8)
                image = ImageFunctions.addition(image1, image2)
                self.createMDISubWindow("Sans Titre " + str(self._subWindowCounter), QPixmap(image))
            dialog.close()

    def substractImage(self):
        liste = self.mdi.subWindowList()
        if len(liste) > 0:
            dialog = AdditionSubstractionDialog(liste)
            dialog.radio_addition.setChecked(True)
            dialog.radio_substract.setChecked(False)
            result = dialog.exec_()
            if result == QDialog.Accepted:
                title1, title2 = dialog.getTitles()
                for sub in liste:
                    if title1 == sub.windowTitle():
                        sub1 = sub
                    if title2 == sub.windowTitle():
                        sub2 = sub
                image1 = sub1.widget().pixmap().toImage()
                image1 = image1.convertToFormat(QImage.Format_Grayscale8)
                image2 = sub2.widget().pixmap().toImage()
                image2 = image2.convertToFormat(QImage.Format_Grayscale8)
                image = ImageFunctions.soustraction(image1, image2)
                self.createMDISubWindow("Sans Titre " + str(self._subWindowCounter), QPixmap(image))
            dialog.close()


    def erosionDilatation(self):
        sub = self.getFocusedSubWindow()
        if sub is not None:
            dialog = ErosionDilatationDialog()
            dialog.radio_carre.setChecked(True)
            dialog.radio_erosion.setChecked(True)
            result = dialog.exec_()
            if result == QDialog.Accepted:
                isErosion, isBoule, dim = dialog.getValues()
                strel = ImageFunctions.createStrel(dim, isBoule)
                image = sub.widget().pixmap().toImage()
                image.convertToFormat(QImage.Format_Grayscale8)
                if isErosion:
                    new_image = ImageFunctions.erosion(image, strel)
                else:
                    new_image = ImageFunctions.dilatation(image, strel)
                self.createMDISubWindow("Sans Titre " + str(self._subWindowCounter), QPixmap(new_image))

    def openingClosing(self):
        sub = self.getFocusedSubWindow()
        if sub is not None:
            dialog = OpeningClosingDialog()
            dialog.radio_carre.setChecked(True)
            dialog.radio_opening.setChecked(True)
            result = dialog.exec_()
            if result == QDialog.Accepted:
                isOpening, isBoule, dim = dialog.getValues()
                strel = ImageFunctions.createStrel(dim, isBoule)
                image = sub.widget().pixmap().toImage()
                image.convertToFormat(QImage.Format_Grayscale8)
                if isOpening:
                    new_image = ImageFunctions.ouverture(image, strel)
                else:
                    new_image = ImageFunctions.fermeture(image, strel)
                self.createMDISubWindow("Sans Titre " + str(self._subWindowCounter), QPixmap(new_image))

    def thinningThicking(self):
        sub = self.getFocusedSubWindow()
        if sub is not None:
            dialog = ThinningThickingDialog()
            dialog.radio_thinning.setChecked(True)
            result = dialog.exec_()
            if result == QDialog.Accepted:
                isThinning, max_iter = dialog.getValues()
                image = sub.widget().pixmap().toImage()
                image.convertToFormat(QImage.Format_Grayscale8)
                if isThinning:
                    strel = ImageFunctions.createThinningStrel()
                    new_image = ImageFunctions.amincissement(image, strel, max_iter)
                else:
                    strel = ImageFunctions.createThickingStrel()
                    new_image = ImageFunctions.epaississement(image, strel, max_iter)
                self.createMDISubWindow("Sans Titre " + str(self._subWindowCounter), QPixmap(new_image))


    def squelettisation(self):
        sub = self.getFocusedSubWindow()
        if sub is not None:
            dialog = SquelettisationDialog()
            dialog.radio_thinning.setChecked(True)
            result = dialog.exec_()
            if result == QDialog.Accepted:
                isThinning = dialog.getValues()
                image = sub.widget().pixmap().toImage()
                image.convertToFormat(QImage.Format_Grayscale8)
                if isThinning:
                    new_image = ImageFunctions.squelettisation_amincissement_homothopique(image)
                else:
                    new_image = ImageFunctions.squelettisation_Lantuejoul(image)
                self.createMDISubWindow("Sans Titre " + str(self._subWindowCounter), QPixmap(new_image))


    def getFocusedSubWindow(self) -> QMdiSubWindow:
        sub = self.mdi.currentSubWindow()
        return sub


##############################################################################
##############################################################################

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()