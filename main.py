import tkinter as tk
import tkinter.filedialog as fd
from tkinter import messagebox

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x600')
        self.root.title('Text Editor 2.0')

        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()

        self.load()

    def load(self):
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack()

        self.mainMenu = tk.Menu(self.root)
        self.root.config(menu=self.mainMenu)
        self.filemenu = tk.Menu(self.mainMenu, tearoff=0)
        self.filemenu.add_command(label='Save as file', command=self.saveFile)
        self.filemenu.add_command(label='Open file', command=self.openFile)
        self.filemenu.add_command(label='Save & Exit', command=self.__exit)
        self.mainMenu.add_cascade(label='File', menu=self.filemenu)

        self.infoFrame = tk.Frame(self.mainFrame)
        self.infoFrame.pack()

        self.pasteButton = tk.Button(self.infoFrame, text='Paste', command=self.pasteText)
        self.pasteButton.grid(row=1, column=0)
        self.copyButton = tk.Button(self.infoFrame, text='Copy selected', command=self.copyText)
        self.copyButton.grid(row=1, column=1)

        self.textFrame = tk.Frame(self.mainFrame)
        self.textFrame.pack()
        self.text = tk.Text(self.textFrame, height=int(self.y/2), width=int(self.x/2))
        self.text.pack()

    def pasteText(self):
        text = self.root.clipboard_get()
        self.text.insert(tk.INSERT, text)
    def copyText(self):
        text = self.text.selection_get()
        self.root.clipboard_append(text)

    def saveFile(self):
        filepath = fd.asksaveasfilename()
        text = self.text.get(0.0, tk.END)
        with open(filepath, 'w+') as file:
            file.write(text)
            file.close()

    def openFile(self):
        filepath = fd.askopenfilename()
        with open(filepath, 'r') as file:
            text = file.read()
            self.text.insert(0.0, text)
            file.close()

    def start(self):
        self.root.protocol("WM_DELETE_WINDOW", self.__exit)
        self.root.mainloop()
    def __exit(self):
        try:
            try:
                self.saveFile()
            except TypeError:
                pass
            self.root.destroy()
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    gui = GUI()
    gui.start()
