import tkinter as tk
from tkinter import filedialog,messagebox

root=tk.Tk()
root.title("Notpad")
root.geometry("820x540")

text_area=tk.Text(root,wrap="word",font=("courier new",11), undo=True)
text_area.pack(fill="both",expand =True)

current_file =[None]

def set_title(path = None):
    if path:
        root.title(f"Notepad | {path}")
    else:
        root.title("Notepad")



def new_file():
    current_file[0] = None
    set_title()


def open_file():
    path =filedialog.askopenfilename(
        title="open",
        filetypes=[
            ("Text Files","*.txt")
            ("Python Files", "*.py")
            ("All Files","*.*")
        ]
    )
    if not path:
        return

    try:
        with open(path,"r",encoding="utf-8") as s:
            content = s.read()
    except:
            