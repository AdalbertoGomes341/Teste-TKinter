import tkinter as tk
from tkinter import messagebox

class MyGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text="Your Message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)
        
        self.menuBar = tk.Menu(self.root)
        
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Close",command=self.on_closing)
        self.actionMenu = tk.Menu(self.menuBar, tearoff=0)
        self.actionMenu.add_command(label="Show Message",command=self.show_message)
        
        self.menuBar.add_cascade(menu=self.fileMenu, label="File")
        self.menuBar.add_cascade(menu=self.actionMenu, label="Action")
        
        
        self.root.config(menu=self.menuBar)
        
        self.text = tk.Text(self.root, height=5, font=("Arial", 16))
        self.text.bind("<KeyPress>", self.shortcut)
        self.text.pack(padx=10, pady=10)
        
        self.checkState = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="Show Message TextBox", font=("Arial", 16), variable=self.checkState)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Show Message", font= ("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.clearButton = tk.Button(self.root, text= "Clear", font= ("Arial", 18), command=self.clear)
        self.clearButton.pack(padx=10, pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def show_message(self):
        if self.checkState.get() == 0:
            print(self.text.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message= self.text.get("1.0", tk.END ))
            
    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()
                        
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
            
    def clear(self):
        self.text.delete("1.0", tk.END)
        
MyGUI()