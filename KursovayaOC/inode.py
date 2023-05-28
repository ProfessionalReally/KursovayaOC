#����� Inode
class Inode:
    #�������������
    def __init__(self, inodenum, mode, uid, atime, typei, blockid):
        self.__inodenum = inodenum #����� �����������
        self.__mode = mode #����� ������� � �����
        self.__uid = uid #������������� ������������-��������� �����
        self.__atime = atime #����� ��������
        self.__typei = typei #��� inode (����, �������)
        self.__blockid = blockid #������ ������ � ������� �������� ����

    #��������� �������� inodenum ��������
    @property
    def inodenum(self):
        return self.__inodenum

    #��������� �������� mode ��������
    @property
    def mode(self):
        return self.__mode

    #��������� �������� uid ��������
    @property
    def uid(self):
        return self.__uid

    #��������� �������� atime ��������
    @property
    def atime(self):
        return self.__atime

    #��������� �������� typei ��������
    @property
    def typei(self):
        return self.__typei

    #��������� �������� blockid ��������
    @property
    def blockid(self):
        return self.__blockid