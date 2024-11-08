class Vehicle:
    def _init_(self, owner, __model,__power, __color):
        self.owner = owner
        self.__model = __model
        self.__power = __power
        self.__color = __color
        self.__COLOR_VARIANTS = ["blue", "red", "black", "white"]

    def get_model(self):
        print("Модель: ", self.__model)

    def get_horsepower(self):
        print("Мощность двигателя: ", self.__power)

    def get_color(self):
        print("Цвет: ", self.__color)

    def print_info(self):
        get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".

class Sedan(Vehicle)
