from tkinter import *
import os
import shutil
from tkinter import filedialog
import tkinter.messagebox as mbox
import easygui


def openwindow():
    read_file = easygui.fileopenbox() 
    return read_file

def open_file():
    read = openwindow() 
    try:
        os.startfile(read) 
    except:
        mbox.showinfo('confirmation',"File not found")
        
def move_file():
    source = openwindow()
    destination = filedialog.askdirectory()
    if source == destination:
        mbox.showinfo('confirmation',"Source and Destination are same")
    else:
        shutil.move(source, destination)
        mbox.showinfo('confirmation',"File moved successfully!!")
           
def rename_file():
    source = openwindow()
    newpath = os.path.dirname(source)
    extension=os.path.splitext(source)[1]
    newName=input("Enter new name of the file ")
    path1 = os.path.join(newpath, newName+extension)
    print(path1)
    os.rename(source,path1) 
    mbox.showinfo('confirmation',"File Renamed successfully!")
        
def copy_file():
    source = openwindow()
    destination = filedialog.askdirectory()
    shutil.copy(source, destination)
    mbox.showinfo('confirmation',"File copied successfully!!")
    
def delete_file():
    source = openwindow()
    file_name = os.splitext(source)
    if os.path.exists(source):
        os.remove(source)
        mbox.showinfo('confirmation',"File deleted successfully")
    else:
        mbox.showinfo('confirmation', file_name + " does not exist")	
    
def CreateFolder():
    Folder = filedialog.askdirectory()
    NewFolder=input("Enter a name for the folder ")
    path = os.path.join(Folder, NewFolder)  
    os.mkdir(path)
    mbox.showinfo("Folder created successfully")
    
def list_files_in_folder():
   i = 0
   folder = filedialog.askdirectory(title='Select the folder whose files you want to list')
   files = os.listdir(os.path.abspath(folder))
   list_files_wn = Toplevel(root)
   list_files_wn.title(f'Files in {folder}')
   list_files_wn.geometry('250x250')
   list_files_wn.resizable(0, 0)
   listbox = Listbox(list_files_wn, selectbackground='SteelBlue', font=("Georgia", 10))
   listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
   scrollbar = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
   scrollbar.pack(side=RIGHT, fill=Y)
   listbox.config(yscrollcommand=scrollbar.set)
   while i < len(files):
       listbox.insert(END, files[i])
       i += 1



# Window Configuration
root = Tk()
root.resizable(0,0)
root.title("File Manager")
root.geometry("900x580+100+30")
root.config(bg="gray12")

heading = Label(root,text="File Manager",font=("Castellar", 28,"bold"),bg="gray12",fg="darkturquoise")
heading.grid(row=1, column=1, pady=20, padx=300)

openbutton = Button(root,text="Open a File",cursor="hand2",font=("times new roman",16,"bold"),command=open_file,fg="darkturquoise",bg="gray18",borderwidth=3)
openbutton.grid(row=2, column=1, pady=10, padx=300)

renamebutton = Button(root,text="Rename a File",cursor="hand2",font=("times new roman",16,"bold"),command=rename_file,fg="darkturquoise",bg="gray18",borderwidth=3)
renamebutton.grid(row=3, column=1, pady=0, padx=300)

movebutton =  Button(root,text="Move a File",cursor="hand2",font=("times new roman",16,"bold"),command=move_file,fg="darkturquoise",bg="gray18",borderwidth=3)
movebutton.grid(row=4, column=1, pady=10, padx=300)

copybutton =  Button(root,text="Copy a File",cursor="hand2",font=("times new roman",16,"bold"),command=copy_file,fg="darkturquoise",bg="gray18",borderwidth=3)
copybutton.grid(row=5, column=1, pady=0, padx=300)

deletebutton = Button(root,text="Delete a File",cursor="hand2",font=("times new roman",16,"bold"),command=delete_file,fg="darkturquoise",bg="gray18",borderwidth=3)
deletebutton.grid(row=6, column=1, pady=10, padx=300)

createfolderbutton = Button(root,text="Create a Folder",cursor="hand2",font=("times new roman",16,"bold"),command=CreateFolder,fg="darkturquoise",bg="gray18",borderwidth=3)
createfolderbutton.grid(row=7, column=1, pady=0, padx=300)

listfilesbutton = Button(root,text="Sort Files in a Folder",cursor="hand2",font=("times new roman",16,"bold"),command=list_files_in_folder,fg="darkturquoise",bg="gray18",borderwidth=3)
listfilesbutton.grid(row=8, column=1, pady=10, padx=300)


root.mainloop()





