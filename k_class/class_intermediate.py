class Car:

    # 정적 변수(static variale)
    # 생성자가 메모리에 올려주는게 아닌 가장 먼저 알아서 메모리에 올려준다
    wheel = 6

    def __init__(self, brand='', color='', price=0):

        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_stop(self):
        print(self.brand + ' 시동 꺼짐')


# mom_car = Car('benz', 'black', 15000)
# daddy_car = Car('BMW', 'Blue', 8000)
#
# mom_car.engine_start()
# daddy_car.engine_start()
#
# print(Car.wheel)

cars = [Car, Car]
mom_car = cars[0]()
daddy_car = cars[1]()
print(mom_car, daddy_car, sep='\n')



