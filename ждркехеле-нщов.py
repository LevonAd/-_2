result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше за b")
        if b > 100:
            raise IndexError("b не може бути більше 100")
        if b == 0:
            raise ZeroDivisionError("b не може бути 0")
        return a/b
    except ValueError as er:
        print(f"ValueError: {er}")
    except IndexError as re:
        print(f"IndexError: {re}")
    except ZeroDivisionError as er2:
        print(f"ZeroDivisionError: {er2}")

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as erorr:
        print(f"Exception: {erorr}")

print(result)
