from PyQt6 import QtCore, QtGui, QtWidgets

from gui.dish_panel.explanation_widget import Explanation
from gui.dish_panel.requirements_widget import Requirements_colony
from gui.dish_panel.source_widget import Select_source
from gui.dish_panel.total_widget import Total


class Dish_panel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.main_VLayout = QtWidgets.QVBoxLayout()
        self.main_VLayout.setContentsMargins(16, 16, 16, 16)
        self.main_VLayout.setSpacing(16)


        self.source_widget = Select_source()

        self.main_VLayout.addWidget(self.source_widget)

        self.main_HLayout = QtWidgets.QHBoxLayout()
        self.main_HLayout.setContentsMargins(0, 0, 0, 0)
        self.main_HLayout.setSpacing(16)

        # ---- requirements_widget ----

        self.requirements_widget = Requirements_colony()
        self.main_HLayout.addWidget(self.requirements_widget)

        self.right_VLayout = QtWidgets.QVBoxLayout()
        self.right_VLayout.setContentsMargins(0, 0, 0, 0)
        self.right_VLayout.setSpacing(16)

        # ---- total_widget ----

        self.total_widget = Total()
        self.right_VLayout.addWidget(self.total_widget)

        self.explanation_widget = Explanation()
        self.right_VLayout.addWidget(self.explanation_widget)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.right_VLayout.addItem(spacerItem3)

        self.main_HLayout.addLayout(self.right_VLayout)

        self.main_VLayout.addLayout(self.main_HLayout)

        self.main_HLayout.setStretch(0, 5)
        self.main_HLayout.setStretch(1, 4)

        self.setLayout(self.main_VLayout)
