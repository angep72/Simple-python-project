# Create a function that uses eval() to compute string expressions.
def compute_expression(expr):
    try:
        result = eval(expr)
        return result
    except Exception as e:
        return f"Error: {e}"

