def robust_calculate(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    return wrapper

def calculate(expression):
    return eval(expression)