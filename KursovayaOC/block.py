#����� Block
class Block:
    #�������������
    def __init__(self, numblock , size):
        self.__numblock = numblock #����� �����
        self.__data = "" #������ �����
        self.__size = size #������ �����

    #��������� �������� numblock ��������
    @property
    def numblock(self):
        return self.__numblock
        
    #��������� �������� data ��������
    @property
    def data(self):
        return self.__data

    #��������� �������� size ��������
    @property
    def size(self):
        return self.__size

    #������ ��� data
    @data.setter
    def data(self, DATA):
        self.__data = DATA

