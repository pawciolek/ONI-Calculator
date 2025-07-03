from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import QHBoxLayout


class Requirements_colony(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        antonF = QFontDatabase.addApplicationFont("../src/assets/font/Anton-Regular.ttf")
        antonFont = QFontDatabase.applicationFontFamilies(antonF)

        self.main_VLayout = QtWidgets.QVBoxLayout()
        self.main_VLayout.setContentsMargins(0, 0, 0, 0)


        self.main_frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.VerticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.VerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.VerticalLayout.setSpacing(8)

        # ---- title frame source ----

        self.title_frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy)
        self.title_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_frame.setStyleSheet("background-color:#7F3D5E;\n"
                                       "border: 2px solid black;\n"
                                       "border-radius:4px;\n"
                                       "padding: 4px 8px;")

        self.HLayout_title = QtWidgets.QHBoxLayout(self.title_frame)
        self.HLayout_title.setContentsMargins(0, 0, 0, 0)
        self.HLayout_title.setSpacing(8)

        # ---- total label name ----

        self.Requirement_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.Requirement_label.sizePolicy().hasHeightForWidth())
        self.Requirement_label.setSizePolicy(sizePolicy)
        self.Requirement_label.setFont(QFont(antonFont[0], 16))
        self.Requirement_label.setStyleSheet("color:white;\n"
                                          "border:none;\n"
                                          "padding:0 0 0 0;")
        self.Requirement_label.setText("Total")
        self.Requirement_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HLayout_title.addWidget(self.Requirement_label)

        self.VerticalLayout.addWidget(self.title_frame)

        # ---- Frame total food list ----

        self.total_food_frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHeightForWidth(self.total_food_frame.sizePolicy().hasHeightForWidth())
        self.total_food_frame.setSizePolicy(sizePolicy)
        self.total_food_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.total_food_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.total_food_frame.setStyleSheet("background-color:#21252F;\n"
                                       "border-radius:4px;\n"
                                       "padding: 8px 8px;")

        self.VLayout_btns = QtWidgets.QVBoxLayout(self.total_food_frame)
        self.VLayout_btns.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.VLayout_btns.setContentsMargins(0, 0, 0, 0)
        self.VLayout_btns.setSpacing(8)

        self.VerticalLayout.addWidget(self.total_food_frame)

        self.main_VLayout.addWidget(self.main_frame)
        self.setLayout(self.main_VLayout)


