#����� Directory     
class Directory:

    #�������������
    def __init__(self, inode, name, parent):
        self.__inode = inode #����������
        self.__name = name #�������� ����������
        self.__parent = parent #��������
        self.__children = [] #����
    
    #��������� �������� inode ��������
    @property
    def inode(self):
        return self.__inode
   
    #��������� �������� name ��������
    @property
    def name(self):
        return self.__name

    #��������� �������� name ��������
    @property
    def parent(self):
        return self.__parent

    #��������� �������� name ��������
    @property
    def children(self):
        return self.__children

    #������ ��� inode
    @inode.setter
    def inode(self, INODE):
        if INODE > 0:
            self.__inode = INODE
        else:
            raise ValueError("Inode cannot be less than zero")

    #������ ��� name
    @name.setter  
    def name(self, NAME):  
        if NAME != 0:
            self.__name = NAME
        else:
            raise ValueError("Name cannot be empty")

    #������ ��� parent
    @parent.setter
    def parent(self, PARENT):
        self.__parent = PARENT

    #�������� child
    def add_child(self, child):
        child.parent = self
        self.__children.append(child)
    
    #������� child
    def remove_child(self, child):
        self.__children.remove(child)
