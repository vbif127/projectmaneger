import pathlib
import time
from datetime import datetime as dt
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import Combobox

from rich.console import Console

from templates.temp_fullstack import fullstack
from templates.temp_minimal import minimal
from templates.temp_standard import standard
import json, os, sys
from dataclasses import dataclass as ds
from pathlib import Path
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("../../"))


def main():
    con = Console()
    root = Tk()
    root.title( "Creating project" )
    root.geometry( "650x300" )

    font = ("Cascadia Code", 14)

    entry_name_lab = Label( root, text="Введите название проекта:", font=font )
    s = StringVar()
    entry_name = Entry( root, width=20, font=font, textvariable=s )

    combo = Combobox(root, font=font, state="readonly" )
    combo[ "values" ] = ("standard", "minimal", "fullstack")
    combo.current( 0 )

    entry_name_lab.place( x=1, y=0 )
    entry_name.place( x=281, y=0 )
    combo.place( x=281, y=70 )

    lab = Label( root, text="", font=font )
    lab.place( x=1, y=30 )
    @ds
    class Form:
        name: str
        path: str
        data_create: str = str(dt.now()).split(" ")[0]



    def add(form: Form):
        print(os.path.abspath("../../result.json"))
        path = Path(os.path.abspath("result.json"))

        a = json.loads(path.read_text(encoding='utf-8'))
        if list(a["names"].keys()).count(form.name) != 1:
            a["names"][form.name] = f"{len(a['project'])}"
            a["project"][f"{len(a['project'])}"] = {
            'name': form.name,
            "path": form.path,
            "data_create": form.data_create
        }

        path.write_text(json.dumps(a, indent=4), encoding='utf-8')
        return a



    def clicked():
        path, n, temp = fd.askdirectory(), entry_name.get(), combo.get()
        print( path )
        try:
            if path != "":
                if temp == "standard":
                    standard( path, n, lab )
                elif temp == "minimal":
                    minimal( path, n, lab )
                elif temp == "fullstack":
                    fullstack( path, n, lab )

                if os.path.exists(f"{path}/{n}/"):
                    a = add(Form(
                        name=n,
                        path=path
                    ))
                    con.print(a)
                # time.sleep(10)
                root.destroy()
                return
            s.set( "" )
        except Exception as e:
            lab.config( text=f"Ошибка:{e}" )
            con.print_exception()


    btn = Button( root, text="Создать", command=clicked, width=15, height=3, font=font )
    btn.place( x=470, y=200 )

    root.mainloop()
