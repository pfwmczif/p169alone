from tkinter import *
from tkinter import ttk
root.geometry("800x800")
root.title("Gui Creator")
root = Tk()



gui_elements = ["Label","Dropdown","Button"]
dropdown = ttk.Combobox(root, state="readonly", values = gui_elements)
dropdown.pack()


class CreateElements:
    
    
    def __init__(self):
            print("This is create Elements class")
            
    def createLabel(self):
            
        label = Label(root,text="A new label has been created using class")
        label.pack()
            
    def createButton(self):
            
        button = Button(root,text="Button", command = self.message)
        class_btn.pack(padx="20",pady="10")
        
    def createDropdown(self):
           values = ["1","2","3",]  
           class_dropdown = ttk.Combobox(root, state="readonly", values = values)
           class_dropdown.pack()
        
    def choose(self):

        
            
            
        def message(self):
        
        
        
    
    
    
             root.mainloop()
        
        
