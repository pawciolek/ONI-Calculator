from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import QHBoxLayout


class Explanation(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        antonF = QFontDatabase.addApplicationFont("../src/assets/font/Anton-Regular.ttf")
        antonFont = QFontDatabase.applicationFontFamilies(antonF)

        self.main_VLayout = QtWidgets.QVBoxLayout()
        self.main_VLayout.setContentsMargins(0, 0, 0, 0)


        self.main_frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
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

        self.total_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.total_label.sizePolicy().hasHeightForWidth())
        self.total_label.setSizePolicy(sizePolicy)
        self.total_label.setFont(QFont(antonFont[0], 16))
        self.total_label.setStyleSheet("color:white;\n"
                                          "border:none;\n"
                                          "padding:0 0 0 0;")
        self.total_label.setText("Explanation")
        self.total_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HLayout_title.addWidget(self.total_label)

        self.VerticalLayout.addWidget(self.title_frame)

        # ---- Frame total food list ----

        self.Explanation_frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.Explanation_frame.sizePolicy().hasHeightForWidth())
        self.Explanation_frame.setSizePolicy(sizePolicy)
        self.Explanation_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Explanation_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.HLayout_btns = QtWidgets.QHBoxLayout(self.Explanation_frame)
        self.HLayout_btns.setContentsMargins(8, 0, 8, 0)
        self.HLayout_btns.setSpacing(8)

        self.Explanation_frame_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHeightForWidth(self.Explanation_frame_label.sizePolicy().hasHeightForWidth())
        self.Explanation_frame_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Explanation_frame_label.setFont(font)
        self.Explanation_frame_label.setStyleSheet("background-color:transparent;\n"
                                             "color:white;\n"
                                             "border:none;\n"
                                             "padding:0 0 0 0;")
        self.Explanation_frame_label.setText("Text")

        self.HLayout_btns.addWidget(self.Explanation_frame_label)
        self.VerticalLayout.addWidget(self.Explanation_frame)

        self.main_VLayout.addWidget(self.main_frame)
        self.setLayout(self.main_VLayout)


