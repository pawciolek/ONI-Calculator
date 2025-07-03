import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6 import QtCore, QtGui, QtWidgets

from gui.dish_panel.dish_panel import Dish_panel
# Importujesz swój widget
from left_settings_panel import Left_settings_panel
from top_select_panel import Top_select_panel

class main_window_app(object):
    def setupUi(self, Dialog):
        Dialog.resize(1300, 700)
        Dialog.setStyleSheet("background-color:#1F222B;")

        self.main_VLayout = QtWidgets.QVBoxLayout()
        self.main_VLayout.setContentsMargins(0, 0, 0, 0)
        Dialog.setLayout(self.main_VLayout)

        self.main_HLayout = QtWidgets.QHBoxLayout()
        self.main_HLayout.setContentsMargins(0, 0, 0, 0)
        self.main_HLayout.setSpacing(0)
        self.main_VLayout.addLayout(self.main_HLayout)

        # ---- left settings panel ----

        self.left_settings_comp = Left_settings_panel()
        self.main_HLayout.addWidget(self.left_settings_comp)

        self.right_VLayout = QtWidgets.QVBoxLayout()
        self.right_VLayout.setContentsMargins(0, 0, 0, 0)

        self.main_HLayout.addLayout(self.right_VLayout)

        # ---- Top selection panel ----

        self.top_panel = Top_select_panel(Dialog)
        self.right_VLayout.addWidget(self.top_panel)

        self.main_dish_panel = Dish_panel()
        self.right_VLayout.addWidget(self.main_dish_panel)

        self.left_settings_comp.data_updated.connect(
            self.top_panel.selectFood.on_data_updated
        )
        initial = self.left_settings_comp.sorter.sort_by_dlc()
        self.left_settings_comp.data_updated.emit(initial)



        # Dystans pionowy (spacer)
        # spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Policy.Minimum,
        #                                    QtWidgets.QSizePolicy.Policy.Expanding)
        # self.right_VLayout.addItem(spacerItem)

        self.main_HLayout.setStretch(0, 5)
        self.main_HLayout.setStretch(1, 7)

        self.retranslateUi(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Oxygen not included - calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = main_window_app()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
