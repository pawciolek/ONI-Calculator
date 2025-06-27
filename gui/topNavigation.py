from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QFont, QFontDatabase

from gui.settingsUI import UI_leftSettings
from selectFoodComp import Ui_selectFood

class Ui_topNavSelect(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Ustawienie podstawowych właściwości formularza


        antonF = QFontDatabase.addApplicationFont("../src/assets/font/Anton-Regular.ttf")
        antonFont = QFontDatabase.applicationFontFamilies(antonF)

        self.leftSettings = UI_leftSettings()
        self.selectFood = Ui_selectFood()


        self.leftSettings.data_updated.connect(self.selectFood.on_data_updated)
        self.selectFood.overlay_hide_signal.connect(self.toggleVisibleOverlay)


        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        # Główna pozioma ramka (layout)

        self.frame = QtWidgets.QFrame()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        # Przycisk "Select Dishes"
        self.selectBtnFood = QtWidgets.QPushButton()

        self.selectBtnFood.setFont(QFont(antonFont[0], 36))
        self.selectBtnFood.setStyleSheet("color:white;\nborder:none;")
        self.selectBtnFood.setObjectName("pushButton")

        self.selectBtnFood.clicked.connect(self.toggleVisibleOverlay)
        self.horizontalLayout_6.addWidget(self.selectBtnFood)

        # Pionowa linia oddzielająca
        self.line = QtWidgets.QFrame()
        self.line.setMaximumSize(QtCore.QSize(16777215, 30))
        self.line.setStyleSheet("background-color:#3D4358;\ncolor:#3D4358;")
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)

        # Layout na tekst po prawej od przycisku
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # Duża etykieta z wartością
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setFont(QFont(antonFont[0], 24))
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)

        # Layout pionowy z drugą etykietą (np. jednostką)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Dystans pionowy (spacer)
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_4.addItem(spacerItem)

        # Druga etykieta, np. "Kcal per Kg"
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setFont(QFont(antonFont[0], 16))
        self.label_4.setStyleSheet("color:#D8D8D8;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        # Dystans między lewą a prawą stroną (rozszerzalny)
        spacerItem1 = QtWidgets.QSpacerItem(163, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)

        # Layout po prawej stronie (ikony narzędzi)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(16)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Pierwszy zestaw: przycisk + podpis "In pot"
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton = QtWidgets.QToolButton()
        self.toolButton.setStyleSheet("border: none;")

        # Ikony do przycisku "In pot"
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPot.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPotClicked.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.On)
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPot.png"), QtGui.QIcon.Mode.Selected,
                       QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgPotClicked.png"), QtGui.QIcon.Mode.Selected,
                       QtGui.QIcon.State.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(42, 40))
        self.toolButton.setCheckable(True)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Podpis pod przyciskiem
        self.label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(QFont(antonFont[0], 12))
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        # Drugi zestaw: przycisk + podpis "Fertilizer"
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_2 = QtWidgets.QToolButton()
        self.toolButton_2.setStyleSheet("border: none;")

        # Ikony przycisku "Fertilizer"
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizer.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizerClicked.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizer.png"),
                        QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgFertilizerClicked.png"),
                        QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(42, 40))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # Podpis "Fertilizer"
        self.label_2 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(QFont(antonFont[0], 12))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        # Trzeci zestaw: przycisk + podpis "Wild"
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolButton_3 = QtWidgets.QToolButton()
        self.toolButton_3.setStyleSheet("border: none;")

        # Ikony przycisku "Wild"
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWild.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWildClicked.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.On)
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWild.png"), QtGui.QIcon.Mode.Selected,
                        QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("../src/assets/btn/optionHarvest/btnImgWildClicked.png"),
                        QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(42, 40))
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        # Podpis "Wild"
        self.label_3 = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(QFont(antonFont[0], 12))
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        # Dodanie całego prawego layoutu do głównego
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.frame.setLayout(self.horizontalLayout_7)
        self.mainLayout.addWidget(self.frame)
        self.setLayout(self.mainLayout)


        # Ustawienie tłumaczeń (dla późniejszej lokalizacji UI)

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
        self.selectBtnFood.setText(_translate("Form", "SELECT DISHES"))
        self.label_5.setText(_translate("Form", "4000"))
        self.label_4.setText(_translate("Form", "Kcal Per Kg"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label.setText(_translate("Form", "In pot"))
        self.toolButton_2.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "FertilIzer"))
        self.toolButton_3.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "wild"))

    def resizeEvent(self, event) -> None:
        self.overlay.setGeometry(0, 0, self.parent().width(), self.parent().height())  # Adjust overlay size dynamically
        super().resizeEvent(event)

    def toggleVisibleOverlay(self):
        if not self.overlay.isVisible():
            self.overlay.show()
        else:
            self.overlay.hide()


