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



##############################################################################
# MainWindow Class is a Multiple Document Interface allowing us to manage
# Multiple windows and in details multiple Images shown in the application
##############################################################################

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

    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Temporary message
        self.statusbar.showMessage("Ready", 3000)

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

    def openFile(self):
        # Get file to load
        file = QFileDialog.getOpenFileName(self, 'Open File', QDir.currentPath(), "Image files (*.jpg *.gif, *.png)")
        file_path = file[0]
        # create a subwindow with the image
        pixmap = QPixmap(file_path)
        self.createMDISubWindow(file_path, pixmap, True)


    def saveFile(self):
        # Logic for saving a file goes here...
        print("TODO")

    def saveAsFile(self):
        # Logic for saving a file goes here...
        print("TODO")

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
        seuil = 100
        image = QPixmap("C:/Users/Ipro/PycharmProjects/AnalyseImage/images/lena.gif").toImage()
        image = image.convertToFormat(QImage.Format_Grayscale8)
        self.createMDISubWindow("Sans Titre "+ str(self._subWindowCounter), QPixmap(image))
        new_image = ImageFunctions.seuillage_haut(image, seuil)
        self.createMDISubWindow("Sans Titre "+str(self._subWindowCounter), QPixmap(new_image))

    def additionImage(self):
        # Logic for cutting content goes here...
        print("TODO")

    def substractImage(self):
        # Logic for cutting content goes here...
        print("TODO")


##############################################################################
##############################################################################

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()