import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import storeFinder
import database
from datetime import date

USER_PATH = os.path.join(os.getcwd(), "UI'S")


USER_PATH = os.path.join(os.getcwd(), "UI'S")

#CONVERSIONS
INCHES_TO_CENTIMETER = 2.54
CENTIMETERES_TO_METER = 100


#verifies if user has enters proper datatype for fields
def verify_input(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False

def go_stores_page():
    store_page = StoresPage()
    widget.addWidget(store_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def go_home_page():
    home_page = StartPage()
    widget.addWidget(home_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def go_health_page():
    health_page = HealthPage()
    widget.addWidget(health_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class StartPage(QDialog):
    def __init__(self):
        super(StartPage, self).__init__()
        user_filepath = os.path.join(USER_PATH, "startPageUI.ui")
        loadUi(user_filepath, self)
        self.storeButton.clicked.connect(lambda: go_stores_page())
        self.healthButton.clicked.connect(lambda: go_health_page())


class StoresPage(QDialog):
    def __init__(self):
        super(StoresPage, self).__init__()
        user_filepath = os.path.join(USER_PATH, "storesUI.ui")
        loadUi(user_filepath, self)
        self.backButton.clicked.connect(lambda: go_home_page())
        self.gymButton.clicked.connect(self.get_nearest_gyms)
        self.pharmacyButton.clicked.connect(self.get_nearest_pharmacies)

    def get_nearest_gyms(self):
        data = storeFinder.get_data("gym", self.locationEntry.text())
        self.data.setText(data)

    def get_nearest_pharmacies(self):
        data = storeFinder.get_data("pharmacies", self.locationEntry.text())
        self.data.setText(data)


class HealthPage(QDialog):
    def __init__(self):
        super(HealthPage, self).__init__()
        user_filepath = os.path.join(USER_PATH, "healthUI.ui")
        loadUi(user_filepath, self)
        self.weightStats.clicked.connect(self.display_weight)
        self.bmiButton.clicked.connect(self.calculate_BMI)
        self.homeButtonHealth.clicked.connect(lambda: go_home_page())
        self.feet.setMinimum(1)
        self.feet.setMaximum(12)
        self.inches.setMinimum(0)
        self.inches.setMaximum(11)
        self.warning.setVisible(False)

    def calculate_BMI(self):
        if verify_input(self.weightEntry.text()):
            total_meters = (((int(self.feet.value()) * 12) + (int(self.inches.value()))) * INCHES_TO_CENTIMETER)/CENTIMETERES_TO_METER
            bmi = float(self.weightEntry.text())/(total_meters**2)
            self.bmi.setText((str(bmi))[:5])
            self.warning.setVisible(False)
        else:
            self.warning.setVisible(True)

    def get_phone_number(self):
        return self.phoneNumberEntry.text()

    def get_date(self):
        dates = self.dateEntry.text().split("-")
        date_object = date(int(dates[0]), int(dates[1]), int (dates[2]))
        return date_object

    def get_reminder_type(self):
        return self.reminderBox.currentText()


    def display_weight(self):
        database.graph_weight()





app = QApplication(sys.argv)
main_window = StartPage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main_window)
widget.setFixedWidth(1250)
widget.setFixedHeight(800)
widget.show()
app.exec_()
