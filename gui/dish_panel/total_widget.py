from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import QHBoxLayout


class Total(QtWidgets.QWidget):
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
        self.total_label.setText("Total")
        self.total_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HLayout_title.addWidget(self.total_label)

        self.VerticalLayout.addWidget(self.title_frame)

        # ---- Frame total food list ----

        self.total_food_frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.total_food_frame.sizePolicy().hasHeightForWidth())
        self.total_food_frame.setSizePolicy(sizePolicy)
        self.total_food_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.total_food_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.HLayout_btns = QtWidgets.QHBoxLayout(self.total_food_frame)
        self.HLayout_btns.setContentsMargins(8, 0, 8, 0)
        self.HLayout_btns.setSpacing(8)

        """
            Tutaj musisz zrrobic wyswietlanie wszystkich skladnikow na dole masz caly wzor przycisku do utworzenia food_btn_frame -> icon / title / amount
        """

        self.food_btn_frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHeightForWidth(self.food_btn_frame.sizePolicy().hasHeightForWidth())
        self.food_btn_frame.setSizePolicy(sizePolicy)
        self.food_btn_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.food_btn_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.food_btn_frame.setStyleSheet("""
                                            QFrame {
                                                background-color: #3D4358;
                                                border: 2px solid black;
                                                border-radius: 4px;
                                                padding:0 0 0 0;
                                            }
                                        """)

        self.HLayout_btn = QtWidgets.QHBoxLayout(self.food_btn_frame)
        self.HLayout_btn.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.HLayout_btn.setContentsMargins(8, 4, 8, 4)
        self.HLayout_btn.setSpacing(8)

        self.ingredient_icon = QtWidgets.QToolButton()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/assets/dishesICon/img.png"))
        self.ingredient_icon.setIcon(icon)
        self.ingredient_icon.setIconSize(QtCore.QSize(50, 30)) # Wielkość ikony
        self.ingredient_icon.setStyleSheet("background-color:transparent;\n"
                                           "color:white;\n"
                                    "border:none;\n"
                                    "padding:0 0 0 0;")
        self.HLayout_btn.addWidget(self.ingredient_icon)

        self.ingredient_name = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHeightForWidth(self.ingredient_name.sizePolicy().hasHeightForWidth())
        self.ingredient_name.setSizePolicy(sizePolicy)
        self.ingredient_name.setFont(QFont(antonFont[0], 16))
        self.ingredient_name.setStyleSheet("background-color:transparent;\n"
                                           "color:white;\n"
                                        "border:none;\n"
                                        "padding:0 0 0 0;")
        self.ingredient_name.setText("Name")
        self.ingredient_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HLayout_btn.addWidget(self.ingredient_name)

        self.line = QtWidgets.QFrame()
        self.line.setMaximumSize(QtCore.QSize(16777215, 20))
        self.line.setStyleSheet("background-color:#585C70;\ncolor:#585C70;\nborder:none;\npadding:0 0 0 0;")
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.HLayout_btn.addWidget(self.line)

        self.ingredient_amount = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHeightForWidth(self.ingredient_amount.sizePolicy().hasHeightForWidth())
        self.ingredient_amount.setSizePolicy(sizePolicy)
        self.ingredient_amount.setFont(QFont(antonFont[0], 16))
        self.ingredient_amount.setStyleSheet("background-color:transparent;\n"
                                             "color:white;\n"
                                            "border:none;\n"
                                            "padding:0 0 0 0;")
        self.ingredient_amount.setText("0")
        self.ingredient_amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.HLayout_btn.addWidget(self.ingredient_amount)





        self.HLayout_btns.addWidget(self.food_btn_frame)
        spacerItem_title = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                                 QtWidgets.QSizePolicy.Policy.Minimum)
        self.HLayout_btns.addItem(spacerItem_title)
        self.VerticalLayout.addWidget(self.total_food_frame)

        self.main_VLayout.addWidget(self.main_frame)
        self.setLayout(self.main_VLayout)


