"""
    GUI for calculator.
"""

from os.path import join
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QApplication,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QGridLayout
)


class View(QMainWindow):
    """Main class: inherits from QMainWindow"""

    def __init__(self):
        super().__init__()

        # General Layout
        self.genralLayout = QVBoxLayout()
        self.genralLayout.setContentsMargins(0, 0, 0, 0)

        # Setup central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.genralLayout)

        # Customize window
        style = """
        *{
            background: #1d1e21;
        }
        """
        self.setWindowIcon(QIcon(join("Icon", "icon.png")))
        self.setWindowTitle("Calculator")
        self.setFixedSize(225, 250)
        self.setStyleSheet(style)

        # Create Widgets
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Create the display for output"""

        style = """
        *{
            color: 'white';
            font-size: 20px;
            font-family: Consolas;
            border: 1.5px solid 'black';
        }
        """

        self.display = QLineEdit()
        self.display.setFixedHeight(60)
        self.display.setAlignment(Qt.Alignment.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(style)
        self.genralLayout.addWidget(self.display)

    def _createButtons(self):
        """Create buttons"""

        self.buttons = {}
        buttonsLayout = QGridLayout()

        style = """
        *{
            %s
            font-size: 20px;
            font-family: Consolas;
            border: 2px solid 'black';
            border-radius: 1px;
        }
        *:hover{
            background: #313537;
        }
        """

        self.buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '=': (3, 4),
        }

        for btnText, pos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            if pos[1] in {3, 4}:
                self.buttons[btnText].setStyleSheet(style % ("color: 'cyan';"))
            else:
                self.buttons[btnText].setStyleSheet(
                    style % ("color: 'white';"))
            buttonsLayout.addWidget(self.buttons[btnText], *pos)

        self.genralLayout.addLayout(buttonsLayout)

    def _setDisplayText(self, text):
        """Set display's text"""
        self.display.setText(text)
        self.display.setFocus()

    def _displayText(self):
        """Get display's text"""
        return self.display.text()

    def _clearDisplay(self):
        """Clear the display"""
        self._setDisplayText('')


app = QApplication([])
