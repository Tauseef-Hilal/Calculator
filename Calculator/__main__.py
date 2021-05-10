"""
    __main__.py
"""

import sys

try:
    from Calculator.view import View, app
    from Calculator.controller import Controller
    from Calculator.model import evaluateExpression
except ModuleNotFoundError:
    print("[ERROR] The program has unmet dependencies!")
    input("Please follow the instructions in README to install dependencies.")
    exit()


def main():
    """Start of the program"""
    view = View()
    view.show()

    model = evaluateExpression
    Controller(view=view, model=model)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
