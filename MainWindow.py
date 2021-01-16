import sys
from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources

#
# Required modules are :
#   - PyQT5
#   - PyQT5-stubs
#   - PyQT5-sip



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
        functionsToolBar.addAction(self.binarize)
        functionsToolBar.addAction(self.binarize)
        functionsToolBar.addAction(self.addition)
        functionsToolBar.addAction(self.substract)

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

    def openFile(self):
        # Get file to load
        file = QFileDialog.getOpenFileName(self, 'Open File', QDir.currentPath(), "Image files (*.jpg *.gif, *.png)")
        file_path = file[0]
        # create a subwindow with the image
        pixmap = QPixmap(file_path)
        self.createMDISubWindow(pixmap, True)


    def saveFile(self):
        # Logic for saving a file goes here...
        self.mdi.subWindowList()[0].widget().setText("<b>File > Save</b> clicked")

    def saveAsFile(self):
        # Logic for saving a file goes here...
        self.mdi.subWindowList()[0].widget().setText("<b>File > SaveAs</b> clicked")

    def copyContent(self):
        # Logic for copying content goes here...
        self.mdi.subWindowList()[0].widget().setText("<b>Edit > Copy</b> clicked")

    def pasteContent(self):
        # Logic for pasting content goes here...
        self.mdi.subWindowList()[0].widget().setText("<b>Edit > Paste</b> clicked")

    def cutContent(self):
        # Logic for cutting content goes here...
        self.mdi.subWindowList()[0].widget().setText("<b>Edit > Cut</b> clicked")

    def createMDISubWindow(self, pixmap, isExistingImage=False):
        sub = QMdiSubWindow()
        label_image = QLabel()
        label_image.setPixmap(pixmap)
        sub.setWidget(label_image)
        self.mdi.addSubWindow(sub)
        sub.show()
        if isExistingImage:
            self._subWindowCounter +=1

    ######################################################
    # When the user clicks on some navbar action
    ######################################################

    def fileBarAction(self, q):
        print("I CLICKED on File ACTION")
        if (q.text() == "New"):
            sub = QMdiSubWindow()
            sub.setWidget(QLabel())
            self.mdi.addSubWindow(sub)
            sub.show()

    def displayBarAction(self, q):
        print("I CLICKED on Display ACTION")
        if q.text() == "Cascade":
            self.mdi.cascadeSubWindows()

        if q.text() == "Tuile":
            self.mdi.tileSubWindows()

##############################################################################
##############################################################################

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()