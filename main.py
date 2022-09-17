import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x600')
        self.root.title('Text Editor 2.0')

        self.load()

    def load(self):
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack()

        self.mainMenu = tk.Menu(self.root)
        self.root.config(menu=self.mainMenu)
        self.filemenu = tk.Menu(self.mainMenu, tearoff=0)
        self.filemenu.add_command(label='Save as file', command=self.saveFile)
        self.filemenu.add_command(label='Open file', command=self.openFile)
        self.mainMenu.add_cascade(label='File', menu=self.filemenu)

        self.buttonsFrame = tk.Frame(self.mainFrame)
        self.buttonsFrame.pack()

        self.textFrame = tk.Frame(self.mainFrame)
        self.textFrame.pack()
        self.text = tk.Text(self.textFrame)
        self.text.pack()


    def saveFile(self):
        pass

    def openFile(self):
        pass

    def start(self):
        self.root.protocol("WM_DELETE_WINDOW", self.__exit)
        self.root.mainloop()
    def __exit(self):
        self.root.destroy()


if __name__ == '__main__':
    gui = GUI()
    gui.start()
