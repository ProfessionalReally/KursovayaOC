from block import *
from file import *
from inode import *
from superBlock import *
from directory import *

import datetime

# Constants
BLOCK_SIZE = 1024

#Класс FileSystem EXT2
class FileSystem:

   #Инициализация
   def __init__(self):
        self.__Files = []
        self.__Directories = []
        self.__Blocks = []
        self.__SuperBLOCK = SuperBlock(BLOCK_SIZE, 0, 0, 0, 0, 0)
        self.__Inodes = []
    
   #Добавить файл
   def add_file(self, DATA, NAME, PARENT):
       NUMBER = len(self.__Blocks)
       BlockNum = []
       #Добавление блока
       if NUMBER == 0:
           for i in range(0, 12):
               self.__Blocks.append(Block(i, BLOCK_SIZE))
               self.__SuperBLOCK.add_block()
               BlockNum.append(i)
       else:
           for i in range(NUMBER, NUMBER+12):
               self.__Blocks.append(Block(i, BLOCK_SIZE))
               self.__SuperBLOCK.add_block()
               BlockNum.append(i)
           

       #Вычисление номера дескриптора
       INODE = len(self.__Inodes) + 1
       #Создание файла
       self.__Files.append(File(INODE, DATA, NAME, PARENT, len(DATA)))
       self.__SuperBLOCK.add_files()
      

       #Создание дескриптора
       self.__Inodes.append(Inode(INODE, "Full", "Admin", datetime.datetime.now(), "File", BlockNum))
       self.__SuperBLOCK.add_inodes()
       

       #Разделение данных по блокам
       LIST = [DATA[i:i+BLOCK_SIZE] for i in range(0, len(DATA), BLOCK_SIZE)]

       if NUMBER == 0:
           for i in range(0, len(LIST)):
                self.__Blocks[i].data = LIST[i]  
       else:
           j = NUMBER
           for i in range(0, len(LIST)):
               self.__Blocks[j].data = LIST[i] 

       #Количество свободных блоков
       self.__SuperBLOCK.freeblocks = 12 - len(LIST)
      
   #Удалить файл
   def delete_file(self, NAMEFILE, NAMEDIRECTORY):
        flag = 0

        #Удаляем файл
        #Проверяет есть такой файл в директории, если да, то flag = 1 и берется его inode
        i = 0
        while i < (len(self.__Files)):
            if self.__Files[i].name == NAMEFILE and self.__Files[i].parent == NAMEDIRECTORY: 
                flag = 1
                INODE = self.__Files[i].inode
                self.__Files.pop(i)
                self.__SuperBLOCK.delete_files()
            else:
                i += 1

        #Удаляем дескриптор
        #Если файл найден, то по inode берутся id блоков
        if flag == 1:
            i = 0
            while i < (len(self.__Inodes)):
                if INODE == self.__Inodes[i].inodenum:
                   BlocksId = self.__Inodes[i].blockid
                   self.__Inodes.pop(i)
                   self.__SuperBLOCK.delete_inodes()
                else:
                    i += 1
            
            #Удаляем блок
            #Берется содержимое блоков по их id
            # удаление элементов из списка в обратном порядке
            for i in reversed(sorted(BlocksId)):
                del self.__Blocks[i]
                self.__SuperBLOCK.delete_block()
                    
            return 1
        if flag == 0:
            return 0

   def edit_file(self, NAMEFILE, NAMEDIRECTORY, NEWNAME, NEWDATA):
       flag = 0

       #Проверяет есть такой файл в директории, если да, то flag = 1 
       for i in range(len(self.__Files)):
            if self.__Files[i].name == NAMEFILE and self.__Files[i].parent == NAMEDIRECTORY: 
                flag = 1
                INODE = self.__Files[i].inode
                self.__Files[i].name = NEWNAME
                self.__Files[i].data = NEWDATA
                self.__Files[i].size = len(NEWDATA)


        #Если файл найден, то по inode берутся id блоков
       if flag == 1:
            for i in range(len(self.__Inodes)):
                if INODE == self.__Inodes[i].inodenum:
                   BlocksId = self.__Inodes[i].blockid

            #Разделение данных по блокам
            LIST = [NEWDATA[i:i+BLOCK_SIZE] for i in range(0, len(NEWDATA), BLOCK_SIZE)]

            j = 0
            for i in range(len(self.__Blocks)):
               if self.__Blocks[i].numblock == BlocksId[j]:
                  self.__Blocks[i].data = LIST[j]
                  j += 1
               
            return 1
       else: 
           return 0

   #Создаем директорию
   def add_directory(self, NAME, PARENT):
       #Вычисление номера дескриптора
       INODE = len(self.__Inodes) + 1

       #Создание дескриптора
       self.__Inodes.append(Inode(INODE, "Full", "Admin", datetime.datetime.now(), "Directory", ""))
       self.__SuperBLOCK.add_inodes()

       #Создание директории
       self.__Directories.append(Directory(INODE, NAME, PARENT))
       self.__SuperBLOCK.add_directories()

    #Удаление директории
   def delete_directory(self, NAMEDIRECTORY):
       i = 0
       #Удаляем директорию
       while i < (len(self.__Directories)):
            if self.__Directories[i].name == NAMEDIRECTORY:
                INODEDIRECTORY = self.__Directories[i].inode
                self.__Directories.pop(i)
                self.__SuperBLOCK.delete_directories()
            else:
                i += 1

       i = 0
        #Удаляем дескриптор
       while i < (len(self.__Inodes)):
           if self.__Inodes[i].inodenum == INODEDIRECTORY:
                self.__Inodes.pop(i)
                self.__SuperBLOCK.delete_inodes()
           else:
               i += 1

       flag = 0
       INODE = []
       countFile = 0
       #Если в директории есть файлы, то их тоже удаляем
       #Проверяет есть такой файл в директории, если да, то flag = 1 и берется его inode
       i = 0
       while i < (len(self.__Files)):
           if self.__Files[i].parent == NAMEDIRECTORY: 
                flag = 1
                INODE.append(self.__Files[i].inode)
                self.__Files.pop(i)
                self.__SuperBLOCK.delete_files()
                countFile += 1
           else:
               i += 1

       if countFile == 0:
            return 1

       j = 0
       BlocksId = []
       #Удаляем дескриптор
       #Если файл найден, то по inode берутся id блоков
       if flag == 1:
            while j < countFile:
                i = 0
                while i < (len(self.__Inodes)):
                    if INODE[j] == self.__Inodes[i].inodenum:
                        for l in range(len(self.__Inodes[i].blockid)):
                           BlocksId.append(self.__Inodes[i].blockid[l])
                        self.__Inodes.pop(i)
                        self.__SuperBLOCK.delete_inodes()
                    else:
                        i += 1
                j += 1 
              

            #Удаляем блок
            #Берется содержимое блоков по их id
            # удаление элементов из списка в обратном порядке
            for i in reversed(sorted(BlocksId)):
                del self.__Blocks[i]
                self.__SuperBLOCK.delete_block()  
            return 1
       if flag == 0:
            return 0

   def HaveFileInMemory(self, NAMEFILE, NAMEDIRECTORY):
    flag = 0

    #Проверяет есть такой файл в директории, если да, то flag = 1 и берется его inode
    for i in range(len(self.__Files)):
        if self.__Files[i].name == NAMEFILE and self.__Files[i].parent == NAMEDIRECTORY: 
            flag = 1
            INODE = self.__Files[i].inode
    #Если файл найден, то по inode берутся id блоков
    if flag == 1:
        for i in range(len(self.__Inodes)):
            if INODE == self.__Inodes[i].inodenum:
               BlocksId = self.__Inodes[i].blockid
        
        BLOCKS = []

        j = 0
        i = 0
        #Берется содержимое блоков по их id
        while i < (len(self.__Blocks)) or j <= 11:

            if BlocksId[j] == self.__Blocks[i].numblock:
                BLOCKS.append(self.__Blocks[i].data)
                j += 1
            if j > 11:
                break 
            i += 1
   
        return BLOCKS
    if flag == 0:
        return 0
                    
   #Возвращаем состояние файловой системы
   def return_superblock(self):
       return self.__SuperBLOCK.blocksize, self.__SuperBLOCK.blockscount, self.__SuperBLOCK.inodescount, self.__SuperBLOCK.freeblocks, self.__SuperBLOCK.filescount, self.__SuperBLOCK.directoriescount

   def return_info_file(self, name, parent):
       flag = 0

       #Проверяет есть такой файл в директории, если да, то flag = 1 и берется его inode
       for i in range(len(self.__Files)):
         if self.__Files[i].name == name and self.__Files[i].parent == parent:
               SIZE = self.__Files[i].size
               INODE = self.__Files[i].inode
               flag = 1
       
        #Если файл найден, то по inode берутся id блоков
       if flag == 1:
            for i in range(len(self.__Inodes)):
                if INODE == self.__Inodes[i].inodenum:
                    return SIZE, self.__Inodes[i].mode, self.__Inodes[i].uid, self.__Inodes[i].atime 
       else: 
           return 0
            

       
        
