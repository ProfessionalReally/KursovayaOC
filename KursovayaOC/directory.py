#Класс Directory     
class Directory:

    #Инициализация
    def __init__(self, inode, name, parent):
        self.__inode = inode #Дескриптор
        self.__name = name #Название дериктории
        self.__parent = parent #Родители
        self.__children = [] #Дети
    
    #Получение значения inode напрямую
    @property
    def inode(self):
        return self.__inode
   
    #Получение значения name напрямую
    @property
    def name(self):
        return self.__name

    #Получение значения name напрямую
    @property
    def parent(self):
        return self.__parent

    #Получение значения name напрямую
    @property
    def children(self):
        return self.__children

    #Сеттер для inode
    @inode.setter
    def inode(self, INODE):
        if INODE > 0:
            self.__inode = INODE
        else:
            raise ValueError("Inode cannot be less than zero")

    #Сеттер для name
    @name.setter  
    def name(self, NAME):  
        if NAME != 0:
            self.__name = NAME
        else:
            raise ValueError("Name cannot be empty")

    #Сеттер для parent
    @parent.setter
    def parent(self, PARENT):
        self.__parent = PARENT

    #Добавить child
    def add_child(self, child):
        child.parent = self
        self.__children.append(child)
    
    #Удалить child
    def remove_child(self, child):
        self.__children.remove(child)
