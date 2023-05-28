#Класс Inode
class Inode:
    #Инициализация
    def __init__(self, inodenum, mode, uid, atime, typei, blockid):
        self.__inodenum = inodenum #Номер дескриптора
        self.__mode = mode #Права доступа к файлу
        self.__uid = uid #Идентификатор пользователя-владельца файла
        self.__atime = atime #Время создания
        self.__typei = typei #Тип inode (файл, каталог)
        self.__blockid = blockid #Номера блоков в котором хранится файл

    #Получение значения inodenum напрямую
    @property
    def inodenum(self):
        return self.__inodenum

    #Получение значения mode напрямую
    @property
    def mode(self):
        return self.__mode

    #Получение значения uid напрямую
    @property
    def uid(self):
        return self.__uid

    #Получение значения atime напрямую
    @property
    def atime(self):
        return self.__atime

    #Получение значения typei напрямую
    @property
    def typei(self):
        return self.__typei

    #Получение значения blockid напрямую
    @property
    def blockid(self):
        return self.__blockid