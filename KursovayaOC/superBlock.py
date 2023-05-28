#Класс SuperBlock
class SuperBlock:

    #Инициализация
    def __init__(self, blocksize, blockscount, inodescount, freeblocks, filescount, directoriescount):
        self.__blocksize = blocksize #Размер блока
        self.__blockscount = blockscount #Количество блоков
        self.__inodescount = inodescount #Количество дескрипторов
        self.__freeblocks = freeblocks #Количество свободных блоков
        self.__filescount = filescount #Количество файлов
        self.__directoriescount = directoriescount #Количество директорий

    #Получение значения blocksize напрямую
    @property
    def blocksize(self):
        return self.__blocksize

    #Получение значения blockscount напрямую
    @property
    def blockscount(self):
        return self.__blockscount

    #Получение значения inodescount напрямую
    @property
    def inodescount(self):
        return self.__inodescount

    #Получение значения freeblocks напрямую
    @property
    def freeblocks(self):
        return self.__freeblocks

    #Получение значения filescount напрямую
    @property
    def filescount(self):
        return self.__filescount

    #Получение значения directoriescount напрямую
    @property
    def directoriescount(self):
        return self.__directoriescount
    
    #+1 к счетчику блоков
    def add_block(self):
        self.__blockscount += 1

    #-1 к счетчику блоков
    def delete_block(self):
        if self.__blockscount != 0:
            self.__blockscount -= 1
        else: 
            raise ValueError("There are no blocks to delete")

    #+1 к счетчику дескрипторов
    def add_inodes(self):
        self.__inodescount += 1

    #-1 к счетчику дескрипторов
    def delete_inodes(self):
        if self.__inodescount != 0:
            self.__inodescount -= 1
        else: 
            raise ValueError("There are no inodes to delete")

    #+1 к счетчику файлов
    def add_files(self):
        self.__filescount += 1

    #-1 к счетчику файлов
    def delete_files(self):
        if self.__filescount != 0:
            self.__filescount -= 1
        else: 
            raise ValueError("There are no files to delete")

    #+1 к счетчику файлов
    def add_directories(self):
        self.__directoriescount += 1

    #-1 к счетчику файлов
    def delete_directories(self):
        if self.__directoriescount != 0:
            self.__directoriescount -= 1
        else: 
            raise ValueError("There are no directories to delete")

    #Сеттер для blockscount
    @blockscount.setter
    def blockscount(self, BLOCKSCOUNT):
        if BLOCKSCOUNT > 0:
            self.__blockscount = BLOCKSCOUNT
        else:
            raise ValueError("Blockscount cannot be less than zero")

    #Сеттер для blockscount
    @inodescount.setter
    def inodescount(self, INODESCOUNT):
        if INODESCOUNT > 0:
            self.__inodescount = INODESCOUNT
        else:
            raise ValueError("Inodescount cannot be less than zero")

    #Сеттер для freeblocks
    @freeblocks.setter
    def freeblocks(self, FREEBLOCKS):
        if FREEBLOCKS > 0:
            self.__freeblocks = FREEBLOCKS
        else:
            raise ValueError("Freeblocks cannot be less than zero")
    
    #Сеттер для filescount
    @filescount.setter
    def filescount(self, FILESCOUNT):
        if FILESCOUNT > 0:
            self.__filescount = FILESCOUNT
        else:
            raise ValueError("Filescount cannot be less than zero")

    #Сеттер для directoriescount
    @directoriescount.setter
    def directoriescount(self, DIRECTORIESCOUNT):
        if DIRECTORIESCOUNT > 0:
            self.__directoriescount = DIRECTORIESCOUNT
        else:
            raise ValueError("Directoriescount cannot be less than zero")