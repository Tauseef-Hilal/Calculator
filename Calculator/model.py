"""
    Logic for calculator
"""


def evaluateExpression(expression):
    """Evaluate an expression"""
    ERROR_MSG = "ERROR!"

    try:
        result = str(round(eval(expression), 3))
    except:
        result = ERROR_MSG
    
    return result
