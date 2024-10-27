from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os


root = Tk()
root.title("converter")
root.geometry("700x500")
text_editor = Text(root, font=("Arial",5))
text_editor.pack(fill="both",expand=1)

# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":

        os.popen('python.exe converter.py '+filepath).read()
        with open("data.data.data","r") as file:
            data = file.read()
        # os.system("python converter.py test12345")
        
        text_editor.delete("1.0", END)
        text_editor.insert("1.0", data)

# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)

open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.pack()
save_button = ttk.Button(text="Сохранить файл", command=save_file)
save_button.pack()

open_file()
root.mainloop()