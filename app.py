from tkinter import * 
from tkinter.scrolledtext import ScrolledText
import tkinter.filedialog
import tkinter.messagebox

root = tkinter.Tk(className="Editor")
textPad = ScrolledText(root,width=100,height=80)

text=Text(root)
text.grid()

def saveas():
    global text  
    t = text.get("1.0", "end-1c")
    savelocation=tkinter.filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

button=Button(root, text="Save", command=saveas) 
button.grid()


root.mainloop()