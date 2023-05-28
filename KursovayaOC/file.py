#����� File
class File:

    #�������������
    def __init__(self, inode, data, name, parent, size):
        self.__inode = inode #����������
        self.__data = data #������
        self.__name = name #�������� �����
        self.__parent = parent #��������
        self.__size = size #������

    #��������� �������� inode ��������
    @property
    def inode(self):
        return self.__inode
    
    #��������� �������� data ��������
    @property
    def data(self):
        return self.__data

    #��������� �������� name ��������
    @property
    def name(self):
        return self.__name

    #��������� �������� parent ��������
    @property
    def parent(self):
        return self.__parent

    #��������� �������� parent ��������
    @property
    def size(self):
        return self.__size

    #������ ��� name
    @name.setter  
    def name(self, NAME):  
        if NAME != 0:
            self.__name = NAME
        else:
            raise ValueError("Name cannot be empty")

    #������ ��� data
    @data.setter
    def data(self, DATA):
        self.__data = DATA
    
    #������ ��� inode
    @inode.setter
    def inode(self, INODE):
        if INODE > 0:
            self.__inode = INODE
        else:
            raise ValueError("Inode cannot be less than zero")
    
    #������ ��� parent
    @parent.setter
    def parent(self, PARENT):
        self.__parent = PARENT

    #������ ��� size
    @size.setter
    def size(self, SIZE):
        if SIZE > 0:
            self.__size = SIZE
        else:
            raise ValueError("size cannot be less than zero")
