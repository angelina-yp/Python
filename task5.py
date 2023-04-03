# Классовая структура
#
# Есть Человек, характеристиками которого являются:
# Имя
# Возраст
# Наличие денег
# Наличие собственного жилья
#
# Человек может:
# Предоставить информацию о себе
# Заработать деньги
# Купить дом
#
# Также же есть Дом, к свойствам которого относятся:
# Площадь
# Стоимость
# Для Дома можно:
# Применить скидку на покупку
#
# Также есть Небольшой Типовой Дом, обязательной площадью 40м2.
class Human:
    # статические поля
    default_name = 'No name'
    default_age = 0
    def __init__(self, name=default_name, age=default_age):
        # динамические поля
        # публичные
        self.name = name
        self.age = age
        # приватные
        self.__money = 0
        self.__house = None
    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')
#  статический метод
    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')
    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')
    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enough money!')

#    приватный метод
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price

class SmallHouse(House):
    default_area = 40
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)
if __name__ == '__main__':
    # информация о статических полях данного класса
    Human.default_info()
    Angelina = Human('Angelina', 31)
    Angelina.info()
    small_house = SmallHouse(8500)
    Angelina.buy_house(small_house,5)
    Angelina.earn_money(5000)
    Angelina.buy_house(small_house, 5)
    Angelina.earn_money(20000)
    Angelina.buy_house(small_house, 5)
    Angelina.info()





  
