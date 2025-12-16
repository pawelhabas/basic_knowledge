#   AttributeError

class Car:
    def __init__(self, brand: str) -> None:
        self.brand = brand

try:
    volvo: Car = Car(brand='Volvo')
    print(volvo.brand)
    print(volvo.fuel_type)
except AttributeError as e:
    print('>>> AttributeError occurred: ', e)
except Exception as e:
    print(type(e), e)
finally:
    print("-*- "*8)