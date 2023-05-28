#Класс Block
class Block:
    #Инициализация
    def __init__(self, numblock , size):
        self.__numblock = numblock #Номер блока
        self.__data = "" #Данные блока
        self.__size = size #Размер блока

    #Получение значения numblock напрямую
    @property
    def numblock(self):
        return self.__numblock
        
    #Получение значения data напрямую
    @property
    def data(self):
        return self.__data

    #Получение значения size напрямую
    @property
    def size(self):
        return self.__size

    #Сеттер для data
    @data.setter
    def data(self, DATA):
        self.__data = DATA

