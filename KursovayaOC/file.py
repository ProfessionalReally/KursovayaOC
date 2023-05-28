#Класс File
class File:

    #Инициализация
    def __init__(self, inode, data, name, parent, size):
        self.__inode = inode #Дескриптор
        self.__data = data #Данные
        self.__name = name #Название файла
        self.__parent = parent #Родитель
        self.__size = size #Размер

    #Получение значения inode напрямую
    @property
    def inode(self):
        return self.__inode
    
    #Получение значения data напрямую
    @property
    def data(self):
        return self.__data

    #Получение значения name напрямую
    @property
    def name(self):
        return self.__name

    #Получение значения parent напрямую
    @property
    def parent(self):
        return self.__parent

    #Получение значения parent напрямую
    @property
    def size(self):
        return self.__size

    #Сеттер для name
    @name.setter  
    def name(self, NAME):  
        if NAME != 0:
            self.__name = NAME
        else:
            raise ValueError("Name cannot be empty")

    #Сеттер для data
    @data.setter
    def data(self, DATA):
        self.__data = DATA
    
    #Сеттер для inode
    @inode.setter
    def inode(self, INODE):
        if INODE > 0:
            self.__inode = INODE
        else:
            raise ValueError("Inode cannot be less than zero")
    
    #Сеттер для parent
    @parent.setter
    def parent(self, PARENT):
        self.__parent = PARENT

    #Сеттер для size
    @size.setter
    def size(self, SIZE):
        if SIZE > 0:
            self.__size = SIZE
        else:
            raise ValueError("size cannot be less than zero")
