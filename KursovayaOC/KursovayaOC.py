# -*- coding: windows-1251 -*-

from tkinter import _setit
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from FileSystem import *


#��������� ������ FileSystem
filesystem = FileSystem()

# ������� ��� ���������� ���������
def add_element(directory, element):
    global Files
    if directory not in Files: # ���� ���������� ��� ��� � �������
       Files[directory] = [] # ������� ����� ������ ������ ��� ���� ����������
    Files[directory].append(element) # ��������� ������� � ��������������� ������ 

# ������� ��� �������� ���������
def remove_element(directory, element):
    global Files
    if directory in Files: # ���� ���������� ���� � �������
        if element in Files[directory]: # ���� ������� ���� � ������
            Files[directory].remove(element) # ������� ������� �� ������

#���������� ����������
def UpdateDirectory():
    # ������� ������ ���������
    dropdown['menu'].delete(0, 'end')  
    dropdownD['menu'].delete(0, 'end')  
    dropdownD1['menu'].delete(0, 'end')
    dropdownDeleteFileD['menu'].delete(0, 'end')
    dropdownDeleteDirectory['menu'].delete(0, 'end')
    dropdownEditFileD['menu'].delete(0, 'end')
    for option in Directories:
        dropdown['menu'].add_command(label=option, command= _setit(var, option))
        dropdownD['menu'].add_command(label=option, command= _setit(varD, option))
        dropdownD1['menu'].add_command(label=option, command= _setit(varD1, option))
        dropdownDeleteFileD['menu'].add_command(label=option, command= _setit(varDeleteFileD, option))
        dropdownDeleteDirectory['menu'].add_command(label=option, command= _setit(varDeleteDirectoryD, option))
        dropdownEditFileD['menu'].add_command(label=option, command= _setit(varEditFileD, option))

#���������� ��������� ������     
def Update():
    BLOCKSIZE, BLOCKSCOUNT, INODESCOUNT, FREEBLOCKS, FILESCOUNT, DIRECTORIESCOUNT = filesystem.return_superblock()

    #BLOCKSIZE
    lbl1 = Label(frame1, text = 'BLOCKSIZE - ') 
    lbl1.grid(column=0, row=2)
    lbl1 = Label(frame1, text = str(BLOCKSIZE)) 
    lbl1.grid(column=1, row=2)

    #BLOCKSCOUNT
    lbl2 = Label(frame1, text = 'BLOCKSCOUNT - ') 
    lbl2.grid(column=0, row=3)
    lbl2 = Label(frame1, text = str(BLOCKSCOUNT)) 
    lbl2.grid(column=1, row=3)

    #INODESCOUNT
    lbl3 = Label(frame1, text = 'INODESCOUNT - ') 
    lbl3.grid(column=0, row=4)
    lbl3 = Label(frame1, text = str(INODESCOUNT)) 
    lbl3.grid(column=1, row=4)

    #FREEBLOCKS
    lbl4 = Label(frame1, text = 'FREEBLOCKS - ') 
    lbl4.grid(column=0, row=5)
    lbl4 = Label(frame1, text = str(FREEBLOCKS))
    lbl4.grid(column=1, row=5)

    #FILESCOUNT
    lbl5 = Label(frame1, text = 'FILESCOUNT - ') 
    lbl5.grid(column=0, row=6)
    lbl5 = Label(frame1, text = str(FILESCOUNT))
    lbl5.grid(column=1, row=6)

    #DIRECTORIESCOUNT
    lbl6 = Label(frame1, text = 'DIRECTORIESCOUNT - ') 
    lbl6.grid(column=0, row=7)
    lbl6 = Label(frame1, text = str(DIRECTORIESCOUNT))
    lbl6.grid(column=1, row=7)

    #��������� ���� �� �������
    NameFile = varF.get()
    NameDirectory = varD1.get()

    #���� ���� �� ����� ����
    flag = 0

    BLOCKS = filesystem.HaveFileInMemory(NameFile, NameDirectory)
    
    if BLOCKS != 0:
        flag = 1
                
    col = 0
    rw = 9
    for i in range(0, 12):
        text_box = Text(frame1, height=2, width=20, bd=2, relief=GROOVE)
        text_box.grid(column = col, row = rw)
        col += 1
        if col == 4:
            rw += 1
            col = 0
        if flag == 1:
            if BLOCKS[i]:
                text_box.insert(END, str(BLOCKS[i]))
        text_box.configure(state="disabled")

#���������� �����
def AddFile():
  global Files, Directories #���� ������ � ����������

  DATA = boxData.get()
  NAME = boxName.get()
  
  if NAME != "":
      PARENT = var.get()
     
      if len(DATA) <= 12288:
          filesystem.add_file(DATA, NAME, PARENT)

          for i in range(len(Directories)):
            if Directories[i] == PARENT:
                add_element(PARENT, NAME)
                remove_element(PARENT, None)
          messagebox.showinfo(title="Information", message="File was created successfully!")
      else: 
          messagebox.showerror(title="Error", message="The file cannot be added, it is over 12kb")
  else:
      messagebox.showerror(title="Error", message="File cannot be created with empty name!")


  boxData.delete("0", END)
  boxName.delete("0", END)
  var.set(Directories[0])

#���������� ����������
def AddDirectory():
    global Directories, Files

    NAME = boxNameD.get()
   
    if NAME != "":
      PARENT = varD.get()
     
      if PARENT != "root":
        filesystem.add_directory(NAME, PARENT)
      else: 
        filesystem.add_directory(NAME, "root")
      add_element(NAME, None)
      messagebox.showinfo(title="Information", message="Directory was created successfully!")
    else:
      messagebox.showerror(title="Error", message="Directory cannot be created with empty name!")

    
    boxNameD.delete("0", END)

    Directories.append(NAME)
    UpdateDirectory()
 
#�������� �����
def DeleteFile():
    global Files
    NAMEDIRECTORY = varDeleteFileD.get()

    if NAMEDIRECTORY != "":
      NAMEFILE = varDeleteFileF.get()
      if NAMEFILE != "":
          if (filesystem.delete_file(NAMEFILE, NAMEDIRECTORY)) == 1:
            if len(Files[NAMEDIRECTORY]) == 1:
                add_element(NAMEDIRECTORY, None)
            values = Files[NAMEDIRECTORY]
            values.remove(NAMEFILE)
            Files[NAMEDIRECTORY] = values

            messagebox.showinfo(title="Information", message="File was deleted successfully!")
          else:
            messagebox.showerror(title="Error", message="File cannot be deleted!")
      else:
          messagebox.showerror(title="Error", message="File field cannot be empty!")
    else:
      messagebox.showerror(title="Error", message="Directory field cannot be empty!")

#�������� ����������
def DeleteDirectory():
    global Files, Directories
    NAMEDIRECTORY = varDeleteDirectoryD.get()
   
    if NAMEDIRECTORY != "":
       if NAMEDIRECTORY != "root":
           if (filesystem.delete_directory(NAMEDIRECTORY)) == 1: 
                if NAMEDIRECTORY in Files:
                    Files.pop(NAMEDIRECTORY)
                Directories.remove(NAMEDIRECTORY)
                UpdateDirectory()
                messagebox.showinfo(title="Information", message="Directory was deleted successfully!")
       else:
           messagebox.showerror(title="Error", message="You can't delete the root directory!")
    else:
      messagebox.showerror(title="Error", message="Directory field cannot be empty!")

#�������������� �����
def EditFile():
    global Files
    
    NAMEDIRECTORY = varEditFileD.get()
    if NAMEDIRECTORY != "":
      NAMEFILE = varEditFileF.get()
      if NAMEFILE != "":
          NEWNAME = boxNameEdit.get()
          if NEWNAME != "":
              NEWDATA = boxDataEdit.get()
              if (filesystem.edit_file(NAMEFILE, NAMEDIRECTORY, NEWNAME, NEWDATA)) == 1:
                values = Files[NAMEDIRECTORY]
                values.remove(NAMEFILE)
                values.append(NEWNAME)
                Files[NAMEDIRECTORY] = values
                messagebox.showinfo(title="Information", message="File was edited successfully!")
              else:
                messagebox.showerror(title="Error", message="File cannot be edited!")
          else:
             messagebox.showerror(title="Error", message="The new filename cannot be empty!")
      else:
          messagebox.showerror(title="Error", message="File field cannot be empty!")
    else:
      messagebox.showerror(title="Error", message="Directory field cannot be empty!")



#������ ����������
Directories = ["root"] 

#������� ������
Files = {}

# ������� ��� ���������� ������ ������ ��� ������ ����������
def update_files(*args): 
    global Files
    current_dir = varD1.get() # �������� ������� ��������� ����������
    dropdownF['menu'].delete(0, 'end') # ������� ������ ������ ������
    for file in Files.get(current_dir, []): # ��������� ����� ������ ������ ��� ��������� ����������
        dropdownF['menu'].add_command(label=file, command=_setit(varF, file))

# ������� ��� ���������� ������ ������ ��� ������ ���������� � ��������
def update_files_delete(*args): 
    global Files
    current_dir = varDeleteFileD.get() # �������� ������� ��������� ����������
    dropdownDeleteFileF['menu'].delete(0, 'end') # ������� ������ ������ ������
    for file in Files.get(current_dir, []): # ��������� ����� ������ ������ ��� ��������� ����������
        dropdownDeleteFileF['menu'].add_command(label=file, command=_setit(varDeleteFileF, file))

# ������� ��� ���������� ������ ������ ��� ������ ���������� � ��������������
def update_files_edit(*args): 
    global Files
    current_dir = varEditFileD.get() # �������� ������� ��������� ����������
    dropdownEditFileF['menu'].delete(0, 'end') # ������� ������ ������ ������
    for file in Files.get(current_dir, []): # ��������� ����� ������ ������ ��� ��������� ����������
        dropdownEditFileF['menu'].add_command(label=file, command=_setit(varEditFileF, file))

# ������� ��� ���������� ������
def update_treeview(data):
    tree.delete(*tree.get_children())  # ������� ������
    parentparent = tree.insert("", "end", text="root", open=True)
    for directory, files in data.items():
        # ���������� ����������
        if directory == 'root':
           for file in files:
                tree.insert(parentparent, "end", text=str(file), open=False)
           continue
        parent = tree.insert(parentparent, "end", text=str(directory), open=False)
        # ���������� ������
        for file in files:
            tree.insert(parent, "end", text=str(file))


def show_info_file():
    # ������� ����� ����
    info_window = Toplevel(root)
    info_window.title('Information File')
    info_window.geometry('300x120')
    # ������������� ����������� ����
    info_window.grab_set()

    #��������� ���� �� �������
    NameFile = varF.get()
    NameDirectory = varD1.get()
    
    if (filesystem.return_info_file(NameFile, NameDirectory)) != 0:
        SIZE, MODE, UID, ATIME = filesystem.return_info_file(NameFile, NameDirectory)

        # ������� ������ Label � �������� ����� � �������������� �������������� �����
        message = f'Directory = {NameDirectory}\nFile = {NameFile}\nSize = {SIZE}\nFile permissions = {MODE}\nFile owner = {UID}\nFile creation time = {ATIME}'
    else:
        message = f'File not found'

    label = Label(info_window, text=message)
    label.pack(pady=10)
    
#�������� �������� ����������
add_element("root", None)

#�������� ����
root = Tk()
root.title('EXT2') #���������

#�������� �������
notebook = ttk.Notebook()  
notebook.pack(expand = True, fill = BOTH)

#������� ���� �������
frame1 = ttk.Frame(notebook, width=700, height=500)  
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand = True)
frame5.pack(fill=BOTH, expand = True)
frame2.pack(fill=BOTH, expand = True)
frame3.pack(fill=BOTH, expand = True)
frame4.pack(fill=BOTH, expand = True)

notebook.add(frame1, text='State Memory')  
notebook.add(frame5, text='Tree')
notebook.add(frame2, text='Add File/Directory') 
notebook.add(frame3, text='Delete File/Directory')
notebook.add(frame4, text='Edit File')


#####FRAME 1 STATE MEMORY

#������� ���������� �� SuperBlock

labelSuperBlock = Label(frame1, text = "   SuperBlock")
labelSuperBlock.config(font=('Helvetica', 14))
labelSuperBlock.grid(column=0, row=0)

#��� ������ ����������
labelDirectoryD = Label(frame1, text="Directory ")
labelDirectoryD.config(font=('Helvetica', 14))
labelDirectoryD.grid(column=2, row=0, ipadx=6, ipady=6)

varD1 = StringVar()
varD1.set(Directories[0])

#�������� ����������� ������ ��� ������ ����������
dropdownD1 = OptionMenu(frame1, varD1, *Directories)
dropdownD1.config(width = 10, font=('Helvetica', 14))
dropdownD1.grid(column=2, row=2, ipadx=6, ipady=6)

#��� ������ �����
labelF = Label(frame1, text="File  ")
labelF.config(font=('Helvetica', 14))
labelF.grid(column=2, row=4, ipadx=6, ipady=6)

varF = StringVar()

#�������� ����������� ������ ��� ������ �����
dropdownF = OptionMenu(frame1, varF, "")
dropdownF.config(width = 10, font=('Helvetica', 14))
dropdownF.grid(column=2, row=6, ipadx=6, ipady=6)

varD1.trace('w', update_files)

#����� ������
labelDirectoryD = Label(frame1, text="BLOCKS(1-12)")
labelDirectoryD.config(font=('Helvetica', 14))
labelDirectoryD.grid(column=2, row=8, ipadx=6, ipady=6)


# ������� ������ ��� �������� ������������ ����
button = Button(root, text='Information File', command=show_info_file)
button.pack(pady=20)

Update()

#�������� ������ ����������
buttonUpdate = Button(frame1, text="Update", command=Update)
buttonUpdate.config(width = 10, font=('Helvetica', 14))
buttonUpdate.grid(column=3, row=4)


#####ADD FILE/DIRECTORY

###FILE � ������� ADD FILE

#����� ��������� FILE
labelFile = Label(frame2, text = "FILE")
labelFile.config(font=('Helvetica', 32))
labelFile.grid(column=0, row=0, ipadx=6, ipady=6)

#��� ����� ������ � �����
labelData = Label(frame2, text="Data ")
labelData.config(font=('Helvetica', 14))
labelData.grid(column=0, row=1, ipadx=6, ipady=6)
boxData = Entry(frame2, width=40)
boxData.grid(column=0, row=2, ipadx=6, ipady=6)

#��� ����� �������� �����
labelName = Label(frame2, text="Name ")
labelName.config(font=('Helvetica', 14))
labelName.grid(column=0, row=3, ipadx=6, ipady=6)
boxName = Entry(frame2, width=40)
boxName.grid(column=0, row=4, ipadx=6, ipady=6)

#��� ����� ���������� �����
labelDirectory = Label(frame2, text="Directory ")
labelDirectory.config(width = 0, font=('Helvetica', 14))
labelDirectory.grid(column=0, row=5, ipadx=6, ipady=6)

#��������� �������� ������ ����������
var = StringVar()
var.set(Directories[0]) 

#�������� ����������� ������ ��� ������ ����������
dropdown = OptionMenu(frame2, var, *Directories)
dropdown.config(width = 18, font=('Helvetica', 14))
dropdown.grid(column=0, row=6, ipadx=6, ipady=6)

#�������� ������ ���������� �����
buttonAddFile = Button(frame2, text="Add File", command=AddFile)
buttonAddFile.config(width = 21, font=('Helvetica', 14))
buttonAddFile.grid(column=0, row=7, ipadx=6, ipady=6)


###DIRECTORY � ������� ADD DIRECTORY

#����� ��������� DIRECTORY
labelDirectory = Label(frame2, text = " DIRECTORY")
labelDirectory.config(font=('Helvetica', 32))
labelDirectory.grid(column=18, row=0, ipadx=6, ipady=6)

#��� ����� �������� ����������
labelNameD = Label(frame2, text="   ")
labelNameD.config(font=('Helvetica', 14))
labelNameD.grid(column=17, row=1, ipadx=6, ipady=6)

labelNameD = Label(frame2, text="  Name ")
labelNameD.config(font=('Helvetica', 14))
labelNameD.grid(column=18, row=1, ipadx=6, ipady=6)
boxNameD = Entry(frame2, width=50)
boxNameD.grid(column=18, row=2, ipadx=6, ipady=6)

#��� ����� �������� ����������
labelDirectoryD = Label(frame2, text="  Directory ")
labelDirectoryD.config(font=('Helvetica', 14))
labelDirectoryD.grid(column=18, row=3, ipadx=6, ipady=6)

varD = StringVar()
varD.set(Directories[0])

#�������� ����������� ������ ��� ������ ��������
dropdownD = OptionMenu(frame2, varD, *Directories)
dropdownD.config(width = 18, font=('Helvetica', 14))
dropdownD.grid(column=18, row=4, ipadx=6, ipady=6)

#�������� ������ ���������� ����������
buttonAddDirectory = Button(frame2, text="Add Directory", command=AddDirectory)
buttonAddDirectory.config(width = 21, font=('Helvetica', 14))
buttonAddDirectory.grid(column=18, row=7, ipadx=6, ipady=6)


#### FRAME 3 DILETE FILE/DIRECTORY

#### FILE IN FILE DELETE

#����� ��������� FILE
labelFile = Label(frame3, text = "FILE")
labelFile.config(font=('Helvetica', 32))
labelFile.grid(column=0, row=0, ipadx=6, ipady=6)

#��� ������ ����������
labelDirectoryD = Label(frame3, text="Directory ")
labelDirectoryD.config(font=('Helvetica', 14))
labelDirectoryD.grid(column=0, row=1, ipadx=6, ipady=6)

#��������� �������� ������ ����������
varDeleteFileD = StringVar()
varDeleteFileD.set(Directories[0])

#�������� ����������� ������ ��� ������ ����������
dropdownDeleteFileD = OptionMenu(frame3, varDeleteFileD, *Directories)
dropdownDeleteFileD.config(width = 10, font=('Helvetica', 18))
dropdownDeleteFileD.grid(column=0, row=2, ipadx=6, ipady=6)

#��� ������ �����
labelF = Label(frame3, text="File  ")
labelF.config(font=('Helvetica', 14))
labelF.grid(column=0, row=3, ipadx=6, ipady=6)

#��������� �������� ������ ����������
varDeleteFileF = StringVar()

#�������� ����������� ������ ��� ������ �����
dropdownDeleteFileF = OptionMenu(frame3, varDeleteFileF, "")
dropdownDeleteFileF.config(width = 10, font=('Helvetica', 18))
dropdownDeleteFileF.grid(column=0, row=4, ipadx=6, ipady=6)

varDeleteFileD.trace('w', update_files_delete)

labelNameD = Label(frame3, text="")
labelNameD.config(font=('Helvetica', 14))
labelNameD.grid(column=0, row=5, ipadx=6, ipady=6)


#�������� ������ ���������� �����
buttonDeleteFile = Button(frame3, text="Delete File", command=DeleteFile)
buttonDeleteFile.config(width = 21, font=('Helvetica', 14))
buttonDeleteFile.grid(column=0, row=8, ipadx=6, ipady=6)


#### DIRECTORY IN DIRECTORY DELETE

#����� ��������� DIRECTORY
labelDirectory = Label(frame3, text = " DIRECTORY")
labelDirectory.config(font=('Helvetica', 32))
labelDirectory.grid(column=18, row=0, ipadx=6, ipady=6)

labelNameD = Label(frame3, text="                    ")
labelNameD.config(font=('Helvetica', 14))
labelNameD.grid(column=17, row=1, ipadx=6, ipady=6)

labelName = Label(frame3, text="Name ")
labelName.config(font=('Helvetica', 14))
labelName.grid(column=18, row=1, ipadx=6, ipady=6)

#��������� �������� ������ ����������
varDeleteDirectoryD = StringVar()
varDeleteDirectoryD.set(Directories[0])

#�������� ����������� ������ ��� ������ ����������
dropdownDeleteDirectory = OptionMenu(frame3, varDeleteDirectoryD, *Directories)
dropdownDeleteDirectory.config(width = 10, font=('Helvetica', 18))
dropdownDeleteDirectory.grid(column=18, row=2, ipadx=6, ipady=6)

#�������� ������ �������� ����������
buttonDeleteDirectory = Button(frame3, text="Delete Directory", command=DeleteDirectory)
buttonDeleteDirectory.config(width = 21, font=('Helvetica', 14))
buttonDeleteDirectory.grid(column=18, row=8, ipadx=6, ipady=6)

#### FRAME 5 TREE

### TREE

tree = ttk.Treeview(frame5)

# ��������� �������� �������
root_node = tree.insert('', END, text = 'root', open = False)

# ���������� ������
update_treeview(Files)

# ����������� ������
tree.pack(expand=True, fill=BOTH)

UpdateTreeButton = Button(frame5, text="Update Tree", command=lambda: update_treeview(Files))
UpdateTreeButton.pack()

#### FRAME 4 EDIT FILE

#����� ��������� FILE
labelFile = Label(frame4, text = "FILE")
labelFile.config(font=('Helvetica', 32))
labelFile.grid(column=0, row=0, ipadx=6, ipady=6)

#��� ������ ����������
labelDirectoryD = Label(frame4, text="Directory ")
labelDirectoryD.config(font=('Helvetica', 14))
labelDirectoryD.grid(column=0, row=1, ipadx=6, ipady=6)

#��������� �������� ������ ����������
varEditFileD = StringVar()
varEditFileD.set(Directories[0])

#�������� ����������� ������ ��� ������ ����������
dropdownEditFileD = OptionMenu(frame4, varEditFileD, *Directories)
dropdownEditFileD.config(width = 10, font=('Helvetica', 18))
dropdownEditFileD.grid(column=0, row=2, ipadx=6, ipady=6)

#��� ������ �����
labelF = Label(frame4, text="File  ")
labelF.config(font=('Helvetica', 14))
labelF.grid(column=0, row=3, ipadx=6, ipady=6)

#��������� �������� ������ ����������
varEditFileF = StringVar()

#�������� ����������� ������ ��� ������ �����
dropdownEditFileF = OptionMenu(frame4, varEditFileF, "")
dropdownEditFileF.config(width = 10, font=('Helvetica', 18))
dropdownEditFileF.grid(column=0, row=4, ipadx=6, ipady=6)

varEditFileD.trace('w', update_files_edit)

labelNameD = Label(frame4, text="")
labelNameD.config(font=('Helvetica', 14))
labelNameD.grid(column=0, row=5, ipadx=6, ipady=6)

#��� ����� ������ � �����
labelData = Label(frame4, text="New Data ")
labelData.config(font=('Helvetica', 14))
labelData.grid(column=2, row=1, ipadx=6, ipady=6)
boxDataEdit = Entry(frame4, width=40)
boxDataEdit.grid(column=2, row=2, ipadx=6, ipady=6)

#��� ����� �������� �����
labelName = Label(frame4, text="New Name ")
labelName.config(font=('Helvetica', 14))
labelName.grid(column=2, row=3, ipadx=6, ipady=6)
boxNameEdit = Entry(frame4, width=40)
boxNameEdit.grid(column=2, row=4, ipadx=6, ipady=6)

#�������� ������ ���������� �����
buttonEditFile = Button(frame4, text="Edit File", command=EditFile)
buttonEditFile.config(width = 14, font=('Helvetica', 14))
buttonEditFile.grid(column=1, row=8, ipadx=6, ipady=6)

root.mainloop()








   













