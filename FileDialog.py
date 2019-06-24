from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(file_path)
