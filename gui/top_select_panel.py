from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QFontDatabase

from gui.left_settings_panel import Left_settings_panel
from dishes_list_menu import Dishes_menu

class Top_select_panel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Ustawienie podstawowych właściwości formularza

        # main font
        antonF = QFontDatabase.addApplicationFont("../src/assets/font/Anton-Regular.ttf")
        antonFont = QFontDatabase.applicationFontFamilies(antonF)

        self.left_panel = Left_settings_panel()
        self.selectFood = Dishes_menu()

        self.left_panel.data_updated.connect(self.selectFood.on_data_updated)
        self.selectFood.overlay_hide_signal.connect(self.toggleVisibleOverlay)
        self.selectFood.selected_name_btn.connect(self.change_name_btn)

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        # Main Frame

        self.frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color:#21252F;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_7.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout_7.setSpacing(300)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")



        # Wewnętrzny layout po lewej stronie
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(16)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # btn "Select Dishes"
        self.selectBtnFood = QtWidgets.QPushButton()

        self.selectBtnFood.setFont(QFont(antonFont[0], 36))
        self.selectBtnFood.setStyleSheet("color:white;\nborder:none;")
        self.selectBtnFood.setObjectName("pushButton")

        # open food list

        self.selectBtnFood.clicked.connect(self.toggleVisibleOverlay)
        self.horizontalLayout_6.addWidget(self.selectBtnFood)

        self.line = QtWidgets.QFrame()
        self.line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.line.setStyleSheet("background-color:#3D4358;\ncolor:#3D4358;")
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.line.hide()
        self.horizontalLayout_6.addWidget(self.line)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # ---- label displaying the amount of calories ---
        self.kcal_amount_label = QtWidgets.QLabel()
        self.kcal_amount_label.setFont(QFont(antonFont[0], 24))
        self.kcal_amount_label.setStyleSheet("color:white;")
        self.kcal_amount_label.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.kcal_amount_label)

        # --------
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Dystans pionowy (spacer)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_4.addItem(spacerItem)

        # ---- second label displaying units of calories ----
        self.kcal_units_label = QtWidgets.QLabel()
        self.kcal_units_label.setFont(QFont(antonFont[0], 16))
        self.kcal_units_label.setStyleSheet("color:#D8D8D8;")
        self.verticalLayout_4.addWidget(self.kcal_units_label)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        # distance between left and right side
        spacerItem1 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)

        # Layout po prawej stronie (ikony narzędzi)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # first set: button + label "In pot"
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # ---- Button "In Pot" ----
        self.potted_select_btn = QtWidgets.QToolButton() # self.potted_selection_button - > variable name
        self.potted_select_btn.setStyleSheet("border: none;")

        # Button icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPot.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPotClicked.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.On)
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPot.png"), QtGui.QIcon.Mode.Selected,
                       QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPotClicked.png"), QtGui.QIcon.Mode.Selected,
                       QtGui.QIcon.State.On)
        self.potted_select_btn.setIcon(icon)
        self.potted_select_btn.setIconSize(QtCore.QSize(42, 40))
        self.potted_select_btn.setCheckable(True)

        self.horizontalLayout.addWidget(self.potted_select_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # label name under button
        self.potted_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.potted_label.sizePolicy().hasHeightForWidth())
        self.potted_label.setSizePolicy(sizePolicy)
        self.potted_label.setFont(QFont(antonFont[0], 12))
        self.potted_label.setStyleSheet("color: white;")
        self.potted_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.potted_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        # Second set: button + label "Fertilizer"
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # ---- Button "Fertilizer" ----
        self.Fertilizer_select_btn = QtWidgets.QToolButton() # self.Fertilizer_select_btn - > variable name
        self.Fertilizer_select_btn.setStyleSheet("border: none;")

        # Button icon "Fertilizer"
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizer.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizerClicked.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizer.png"),
                        QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizerClicked.png"),
                        QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.Fertilizer_select_btn.setIcon(icon1)
        self.Fertilizer_select_btn.setIconSize(QtCore.QSize(42, 40))
        self.Fertilizer_select_btn.setCheckable(True)
        self.horizontalLayout_2.addWidget(self.Fertilizer_select_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # label name "Fertilizer"
        self.Fertilizer_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.Fertilizer_label.sizePolicy().hasHeightForWidth())
        self.Fertilizer_label.setSizePolicy(sizePolicy)
        self.Fertilizer_label.setFont(QFont(antonFont[0], 12))
        self.Fertilizer_label.setStyleSheet("color: white;")
        self.Fertilizer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2.addWidget(self.Fertilizer_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        # third set: button + label "Wild"
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # --- Button "Wild" ----
        self.wild_select_btn = QtWidgets.QToolButton() # self.wild_select_btn - > variable name
        self.wild_select_btn.setStyleSheet("border: none;")

        # Button icon "Wild"
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWild.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWildClicked.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWild.png"), QtGui.QIcon.Mode.Selected,
                        QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWildClicked.png"),
                        QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.wild_select_btn.setIcon(icon2)
        self.wild_select_btn.setIconSize(QtCore.QSize(42, 40))
        self.wild_select_btn.setCheckable(True)
        self.wild_select_btn.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.wild_select_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        # label name "Wild"
        self.wild_label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.wild_label.sizePolicy().hasHeightForWidth())
        self.wild_label.setSizePolicy(sizePolicy)
        self.wild_label.setFont(QFont(antonFont[0], 12))
        self.wild_label.setStyleSheet("color: white;")
        self.wild_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wild_label.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.wild_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.frame.setLayout(self.horizontalLayout_7)
        self.mainLayout.addWidget(self.frame)
        self.setLayout(self.mainLayout)

        # overlay to show food list menu
        self.overlay = QtWidgets.QWidget(self.parent())
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.5)")
        self.overlay.setGeometry(0, 0, self.parent().width(), self.parent().height())
        self.overlay.hide()

        self.overlay_HLayout = QtWidgets.QHBoxLayout()
        self.overlay_HLayout.setContentsMargins(0, 0, 0, 0)
        self.overlay.setLayout(self.overlay_HLayout)

        spacerItem2 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.overlay_HLayout.addItem(spacerItem2)

        self.overlay_HLayout.addWidget(self.selectFood)

        spacerItem3 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.overlay_HLayout.addItem(spacerItem3)


        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate

        self.potted_select_btn.setText(_translate("Form", "..."))
        self.potted_label.setText(_translate("Form", "In pot"))
        self.Fertilizer_select_btn.setText(_translate("Form", "..."))
        self.Fertilizer_label.setText(_translate("Form", "FertilIzer"))
        self.wild_select_btn.setText(_translate("Form", "..."))
        self.wild_label.setText(_translate("Form", "wild"))

    def resizeEvent(self, event) -> None:
        self.overlay.setGeometry(0, 0, self.parent().width(), self.parent().height())  # Adjust overlay size dynamically
        super().resizeEvent(event)

    def toggleVisibleOverlay(self):
        """
        Change the state of "self.overlay" after clicking the button that opens the list of dishes.
        Opens the list of dishes to choose from and sets the background to full width black

        :return: "self.overlay.show()" or "self.overlay.hide()"
        """
        if not self.overlay.isVisible():
            self.overlay.raise_()
            self.overlay.show()
        else:
            self.overlay.hide()

    def change_name_btn(self, name_list):
        """
        the function changes the state of the button name and icon after selecting a dish from the list of dishes.

        :param name_list: data from selected dish
        :return: changes the name of the button and icon, amount calories label and unit calories label
        """
        if name_list:
            self.selectBtnFood.setText(name_list[0])
            self.kcal_amount_label.setText(str(name_list[1]))
            if name_list[1]:
                self.kcal_units_label.setText("Kcal Per Kg")
                self.line.show()
            else:
                self.kcal_units_label.setText("")
                self.line.hide()
        else:
            self.selectBtnFood.setText("SELECT DISH")
            self.kcal_amount_label.setText("")




