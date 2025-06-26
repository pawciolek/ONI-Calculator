import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6 import QtCore, QtGui, QtWidgets

# Importujesz swój widget
from settingsUI import UI_leftSettings
from topNavigation import Ui_topNavSelect

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 600)
        Dialog.setStyleSheet("background-color:#1F222B;")

        self.main_VLayout = QtWidgets.QVBoxLayout()
        self.main_VLayout.setContentsMargins(0, 0, 0, 0)
        Dialog.setLayout(self.main_VLayout)

        self.main_HLayout = QtWidgets.QHBoxLayout()
        self.main_HLayout.setContentsMargins(0, 0, 0, 0)
        self.main_HLayout.setSpacing(0)
        self.main_VLayout.addLayout(self.main_HLayout)

        self.left_settings_widget = QtWidgets.QWidget()
        self.left_settings_comp = UI_leftSettings()
        self.left_settings_comp.setupUi(self.left_settings_widget)
        self.main_HLayout.addWidget(self.left_settings_widget)

        self.right_VLayout = QtWidgets.QVBoxLayout()
        self.right_VLayout.setContentsMargins(0, 0, 0, 0)
        self.main_HLayout.addLayout(self.right_VLayout)

        self.top_nav_comp = Ui_topNavSelect(Dialog)
        self.right_VLayout.addWidget(self.top_nav_comp)

        # Dystans pionowy (spacer)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.right_VLayout.addItem(spacerItem)

        self.main_HLayout.setStretch(0, 5)
        self.main_HLayout.setStretch(1, 7)

        self.retranslateUi(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kliker"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
