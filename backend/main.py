import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import storeFinder


def go_stores_page():
    store_page = StoresPage()
    widget.addWidget(store_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def go_home_page():
    home_page = StartPage()
    widget.addWidget(home_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class StartPage(QDialog):
    def __init__(self):
        super(StartPage, self).__init__()
        loadUi(r"C:\Users\Desktop\Desktop\Backend\UI\startPageUI.ui", self)
        self.storeButton.clicked.connect(lambda: go_stores_page())


class StoresPage(QDialog):
    def __init__(self):
        super(StoresPage, self).__init__()
        loadUi(r"C:\Users\Desktop\Desktop\Backend\UI\storesUI.ui", self)
        self.backButton.clicked.connect(lambda: go_home_page())
        self.gymButton.clicked.connect(self.get_nearest_gyms)
        self.pharmacyButton.clicked.connect(self.get_nearest_pharmacies)

    def get_nearest_gyms(self):
        data = storeFinder.get_data("gym", self.locationEntry.text())

        self.data.setText(data)

    def get_nearest_pharmacies(self):
        data = storeFinder.get_data("pharmacies", self.locationEntry.text())
        self.data.setText(data)


app = QApplication(sys.argv)
main_window = StartPage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedWidth(1250)
widget.setFixedHeight(800)
widget.show()
app.exec_()
