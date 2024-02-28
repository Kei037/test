# MILES, POUND 단위 변환에서 사용하는 변수
MILES = 0.621371
POUND = 0.00220462


def kilometer_to_miles(kilograms: int | float) -> float:
    """ 킬로미터를 마일로 변환 """
    return kilograms * MILES


def grams_to_pounds(grams: int | float) -> float:
    """ 그램을 파운드로 변환하는 함수 """
    return grams * POUND
