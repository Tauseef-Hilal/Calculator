"""
    Controller for view.py
"""

from functools import partial


class Controller():
    """Controller class"""

    def __init__(self, view, model):
        self._view = view
        self._evaluate = model
        self._connectSignals()
    
    def _calculateResult(self):
        """Evaluate expression"""
        result = self._evaluate(expression=self._view._displayText())
        self._view._setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression"""
        if self._view._displayText() == "ERROR!":
            self._view._clearDisplay()

        expression = f"{self._view._displayText()}{sub_exp}"
        self._view._setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots"""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        
        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view._clearDisplay)
