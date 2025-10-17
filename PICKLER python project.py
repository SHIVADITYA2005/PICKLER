import tkinter as tk
from tkinter import filedialog as fd
import pickle
from datetime import datetime as dt #just for fun
import socket as so #for fun
class Applications(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PICKLER")
        container=tk.Frame(self) #widget to hold all the frames on self(the main window)
        container.pack(side="top",fill="both",expand=True)

        self.frames={}#dictionary to hold all the frames

        for num in (Welcome,Uploader,Pickler):
            throw = num(container,self)#create an object of each frame
            self.frames[num]=throw  #Key num(name) → the class itself (Welcome, Uploader, Pickler) || throw → the object (instance) of that class (like <Welcome object>, <Uploader object>)
            throw.grid(row=0,column=0,sticky="nsew")
        
        self.show_frame(Welcome)
    
    def show_frame(self,page_class):#function to show a particular frame for a given class
        frame=self.frames[page_class]
        frame.tkraise()
    

class Welcome(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        tk.Label(self,text="WELCOME TO PICKLER").pack(padx=100,pady=10)
        now = dt.now() #just for fun
        hostname = so.gethostname()
        ip = so.gethostbyname(hostname)
        tk.Label(self,text=f"{now}").pack(padx=100,pady=10)
        tk.Label(self,text=f"{ip}").pack(side='bottom',padx=50,pady=10,anchor='se')
        tk.Button(self,text="START",command=lambda: controller.show_frame(Uploader)).pack(padx=150,pady=10)

class Uploader(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        tk.Label(self,text="UPLOAD YOUR FILES HERE").pack(padx=100,pady=10)
        tk.Button(self,text="Upload",command=self.upload_files).pack(padx=150,pady=10)
        self.filepath=tk.Label(self,text="No file selected")#default no file is selected
        self.filepath.pack(padx=150,pady=10)
        tk.Button(self,text="NEXT",command=lambda: controller.show_frame(Pickler)).pack(padx=150,pady=10)
    
    def upload_files(self):
        file = fd.askopenfilename(title="select a file",filetypes=(("all files","*.*"),("text files","*.txt*"),("python files","*.py*"),("image files","*.jpg*"),("excel files","*.xlsx*")),multiple=False)
        if file:
            self.filepath.config(text="1 file selected")
            self.controller.shared_file = file 

   
class Pickler(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        tk.Button(self,text="PICKLE",command=self.pickle_files).pack(padx=150,pady=10)
        tk.Button(self,text="UNPICKLE",command=self.unpickle_files).pack(padx=150,pady=10)
        self.final = tk.Label(self,text="No action performed yet")
    def pickle_files(self):
        file =  self.controller.shared_file
        with open(file,"rb") as f:
            file_content=f.read()
        result = fd.asksaveasfilename()
        with open(f"{result}.pkl","wb") as p:
            pickle.dump(file_content,p)
        self.final.config(text="file pickled and saved")
        self.final.pack(padx=150,pady=10)
    
    def unpickle_files(self):
        file =  self.controller.shared_file
        resul = fd.asksaveasfilename()
        with open(file,"rb") as f:
            resul=pickle.load(f)
        self.final.config(text="file unpickled and saved")
        self.final.pack(padx=150,pady=10)
    
   
    
if __name__ == "__main__":
    app = Applications()
    app.mainloop()