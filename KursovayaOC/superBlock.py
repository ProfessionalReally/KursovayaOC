#����� SuperBlock
class SuperBlock:

    #�������������
    def __init__(self, blocksize, blockscount, inodescount, freeblocks, filescount, directoriescount):
        self.__blocksize = blocksize #������ �����
        self.__blockscount = blockscount #���������� ������
        self.__inodescount = inodescount #���������� ������������
        self.__freeblocks = freeblocks #���������� ��������� ������
        self.__filescount = filescount #���������� ������
        self.__directoriescount = directoriescount #���������� ����������

    #��������� �������� blocksize ��������
    @property
    def blocksize(self):
        return self.__blocksize

    #��������� �������� blockscount ��������
    @property
    def blockscount(self):
        return self.__blockscount

    #��������� �������� inodescount ��������
    @property
    def inodescount(self):
        return self.__inodescount

    #��������� �������� freeblocks ��������
    @property
    def freeblocks(self):
        return self.__freeblocks

    #��������� �������� filescount ��������
    @property
    def filescount(self):
        return self.__filescount

    #��������� �������� directoriescount ��������
    @property
    def directoriescount(self):
        return self.__directoriescount
    
    #+1 � �������� ������
    def add_block(self):
        self.__blockscount += 1

    #-1 � �������� ������
    def delete_block(self):
        if self.__blockscount != 0:
            self.__blockscount -= 1
        else: 
            raise ValueError("There are no blocks to delete")

    #+1 � �������� ������������
    def add_inodes(self):
        self.__inodescount += 1

    #-1 � �������� ������������
    def delete_inodes(self):
        if self.__inodescount != 0:
            self.__inodescount -= 1
        else: 
            raise ValueError("There are no inodes to delete")

    #+1 � �������� ������
    def add_files(self):
        self.__filescount += 1

    #-1 � �������� ������
    def delete_files(self):
        if self.__filescount != 0:
            self.__filescount -= 1
        else: 
            raise ValueError("There are no files to delete")

    #+1 � �������� ������
    def add_directories(self):
        self.__directoriescount += 1

    #-1 � �������� ������
    def delete_directories(self):
        if self.__directoriescount != 0:
            self.__directoriescount -= 1
        else: 
            raise ValueError("There are no directories to delete")

    #������ ��� blockscount
    @blockscount.setter
    def blockscount(self, BLOCKSCOUNT):
        if BLOCKSCOUNT > 0:
            self.__blockscount = BLOCKSCOUNT
        else:
            raise ValueError("Blockscount cannot be less than zero")

    #������ ��� blockscount
    @inodescount.setter
    def inodescount(self, INODESCOUNT):
        if INODESCOUNT > 0:
            self.__inodescount = INODESCOUNT
        else:
            raise ValueError("Inodescount cannot be less than zero")

    #������ ��� freeblocks
    @freeblocks.setter
    def freeblocks(self, FREEBLOCKS):
        if FREEBLOCKS > 0:
            self.__freeblocks = FREEBLOCKS
        else:
            raise ValueError("Freeblocks cannot be less than zero")
    
    #������ ��� filescount
    @filescount.setter
    def filescount(self, FILESCOUNT):
        if FILESCOUNT > 0:
            self.__filescount = FILESCOUNT
        else:
            raise ValueError("Filescount cannot be less than zero")

    #������ ��� directoriescount
    @directoriescount.setter
    def directoriescount(self, DIRECTORIESCOUNT):
        if DIRECTORIESCOUNT > 0:
            self.__directoriescount = DIRECTORIESCOUNT
        else:
            raise ValueError("Directoriescount cannot be less than zero")