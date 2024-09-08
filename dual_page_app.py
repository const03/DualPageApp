import sys

from PyQt5 import QtWidgets, uic

from constants import (CLEAR_OR_CONVERT_BUTTON_PRESSED,
                       CLEAR_OR_CONVERT_BUTTON_RELEASED, CONVERTER_ERROR,
                       DEFAULT_RESULT_VALUE, LOGIN_BUTTON_PRESSED,
                       LOGIN_BUTTON_RELEASED, LOGIN_ERROR,
                       LOGOUT_BUTTON_PRESSED, LOGOUT_BUTTON_RELEASED, RATES,
                       RESULT_LABEL, UI_FILE, USERS)


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi(UI_FILE, self)
        self.stacked_widget.setCurrentWidget(self.login_page)

        self.login_button.clicked.connect(self.login)
        self.logout_button.clicked.connect(self.logout)
        self.clear_button.clicked.connect(self.clear)
        self.convert_button.clicked.connect(self.convert)

        self.login_button.released.connect(self.login_button_released)
        self.login_button.pressed.connect(self.login_button_pressed)

        self.logout_button.released.connect(self.logout_button_released)
        self.logout_button.pressed.connect(self.logout_button_pressed)

        self.clear_button.released.connect(self.clear_button_released)
        self.clear_button.pressed.connect(self.clear_button_pressed)

        self.convert_button.released.connect(self.convert_button_released)
        self.convert_button.pressed.connect(self.convert_button_pressed)

        # show the app
        self.show()

    def login(self) -> None:
        self.login_error_label.setText("")

        username = self.username.text()
        password = self.password.text()

        if (username, password) in USERS.items():
            self.stacked_widget.setCurrentWidget(self.converter_page)
        else:
            self.login_error_label.setText(LOGIN_ERROR)

    def logout(self) -> None:
        self.login_error_label.setText("")
        self.username.setText("")
        self.password.setText("")
        self.stacked_widget.setCurrentWidget(self.login_page)
        self.clear()

    def clear(self) -> None:
        self.amount.setText("")
        self.result_label.setText(RESULT_LABEL + str(DEFAULT_RESULT_VALUE))
        self.combo_1.setCurrentIndex(0)
        self.combo_2.setCurrentIndex(0)
        self.converter_error_label.setText("")

    def convert(self) -> None:
        self.converter_error_label.setText("")
        from_currency = self.combo_1.currentText()
        to_currency = self.combo_2.currentText()
        try:
            amount = float(self.amount.text())
        except ValueError:
            self.converter_error_label.setText(CONVERTER_ERROR)
            return
        rate = RATES[(from_currency, to_currency)]
        ans = amount * rate
        self.result_label.setText(RESULT_LABEL + str(ans)[:10])

    def login_button_released(self) -> None:
        self.login_button.setStyleSheet(LOGIN_BUTTON_RELEASED)

    def login_button_pressed(self) -> None:
        self.login_button.setStyleSheet(LOGIN_BUTTON_PRESSED)

    def logout_button_released(self) -> None:
        self.logout_button.setStyleSheet(LOGOUT_BUTTON_RELEASED)

    def logout_button_pressed(self) -> None:
        self.logout_button.setStyleSheet(LOGOUT_BUTTON_PRESSED)

    def clear_button_released(self) -> None:
        self.clear_button.setStyleSheet(CLEAR_OR_CONVERT_BUTTON_RELEASED)

    def clear_button_pressed(self) -> None:
        self.clear_button.setStyleSheet(CLEAR_OR_CONVERT_BUTTON_PRESSED)

    def convert_button_released(self) -> None:
        self.convert_button.setStyleSheet(CLEAR_OR_CONVERT_BUTTON_RELEASED)

    def convert_button_pressed(self) -> None:
        self.convert_button.setStyleSheet(CLEAR_OR_CONVERT_BUTTON_PRESSED)


app = QtWidgets.QApplication(sys.argv)
ui_window = UI()
app.exec_()
