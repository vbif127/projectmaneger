import json
import os
import shutil
import sys
from datetime import datetime as dt
from pathlib import Path
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms

from rich.console import Console


sys.path.append( os.path.abspath( "." ) )
sys.path.append( os.path.abspath( ".." ) )
sys.path.append( os.path.abspath( "../../" ) )
sys.path.append( os.path.abspath( "func/gen_project_v2" ) )
sys.path.append( os.path.abspath( "func/gen_project_v2/templates" ) )
from func.gen_project_v2.main import main as create


con = Console()

root = Tk()
root.title( 'PythonGuides' )
root.geometry( '400x300' )
# root.config(bg='#4A7A8C')

frame = Frame( root, height=300, relief=SOLID )
frame.place( x=1, y=1 )

lb = Listbox( frame, font=12, height=15, relief=SOLID )
sb = Scrollbar( frame, orient=VERTICAL, relief=SOLID )
create_btn = Button( text="Создать", height=2, width=12, relief=RAISED,
    command=create )

font = ("Cascadia Code", 14)


def update():
    global names
    lb.delete( 0, len( names ) - 1 )

    try:
        path = Path( 'result.json' )
        a = json.loads( path.read_text( encoding='utf-8' ) )
        names = list( a[ "names" ].keys() )
    except:
        names = [ "Нет проектов" ]
    for i in names:
        lb.insert( END, i )


def delete():
    try:
        global names
        path = Path( 'result.json' )
        b = json.loads( path.read_text( encoding='utf-8' ) )
        print( b )

        a = lb.curselection()
        yes_no = ms.askyesno( message="Вы точно хотите удалить этот проект" )
        if yes_no and b[ "project" ][ f"{a[ 0 ]}" ][ "path" ]:
            print()
            print( a[ 0 ], b[ "project" ] )
            print( b[ "project" ][ f"{a[ 0 ]}" ][ "name" ] )
            shutil.rmtree( f'{b[ "project" ][ f"{a[ 0 ]}" ][ "path" ]}/{b[ "project" ][ f"{a[ 0 ]}" ][ "name" ]}' )
            b[ "names" ].pop( b[ "project" ][ f"{a[ 0 ]}" ][ "name" ] )
            b[ "project" ].pop( str( a[ 0 ] ) )

        path.write_text( json.dumps( b, indent=4 ), encoding='utf-8' )

        print( a, type( a ) )
    except Exception as e:
        ms.showwarning( title="Ошибка", message=f"Ошибка: {e}" )


def openproject():
    try:
        root = Tk()
        root.title( "Информация о проекте" )
        root.geometry( f"{400}x{300}" )
        count = 0
        path = Path( 'result.json' )
        b = json.loads( path.read_text( encoding='utf-8' ) )
        a = lb.curselection()

        info = { "name": b[ "project" ][ f"{a[ 0 ]}" ][ "name" ], "path": b[ "project" ][ f"{a[ 0 ]}" ][ "path" ],
            "to_create": b[ "project" ][ f"{a[ 0 ]}" ][ "data_create" ] }
        lab_info = [ Label( root, text=f'Имя: {info[ "name" ]}', font=font ),
            Label( root, text=f'Путь: {info[ "path" ]}', font=font ),
            Label( root, text=f'Дата создания: {info[ "to_create" ]}', font=font ) ]
        var = { "vsCode": BooleanVar(), "pyCharm": BooleanVar(), "explorer": BooleanVar() }

        command_check = { "vsCode": lambda: var[ "vsCode" ].set( 1 ), "pyCharm": lambda: var[ "pyCharm" ].set( 1 ),
            "explorer": lambda: var[ "explorer" ].set( 1 ), }

        open_check = { "vsCode": Checkbutton( root, text="vsCode", font=font, command=command_check[ "vsCode" ] ),
            "pycharm": Checkbutton( root, text="pycharm", font=font, command=command_check[ "pyCharm" ] ),
            "explorer": Checkbutton( root, text="Проводник", font=font, command=command_check[ "explorer" ] ) }

        def ok():
            # print("----------------")
            project = f'{b[ "project" ][ f"{a[ 0 ]}" ][ "path" ]}/{b[ "project" ][ f"{a[ 0 ]}" ][ "name" ]}'
            print(project)
            if var[ "vsCode" ].get():
                os.system( f"code {project}" )
            if var[ "pyCharm" ].get():
                os.system( f"pycharm {project}" )
            if var[ "explorer" ].get():
                os.system( f"files {project}" )
            root.destroy()

        btn = Button( root, text="Ok", font=font, width=10, command=ok )

        lab_info[ 0 ].place( x=1, y=1 )
        lab_info[ 1 ].place( x=1, y=30 )
        lab_info[ 2 ].place( x=1, y=60 )
        open_check[ "vsCode" ].place( x=1, y=100 )
        open_check[ "pycharm" ].place( x=105, y=100 )
        open_check[ "explorer" ].place( x=230, y=100 )
    except:
        con.print_exception()

    btn.place( x=0, y=150 )

    root.mainloop()

def loadFinishProject():
    pathProject = fd.askdirectory()

    path = Path( 'result.json' )
    b = json.loads( path.read_text( encoding='utf-8' ) )
    b["names"][[(a := pathProject.split("/"))[len(a)-1]][0]] = f"{ len( b[ 'project' ] ) }"


    prpath = pathProject.split("/")
    prpath = prpath[:len(prpath)-1]
    prpath = "/".join(prpath)
    print(prpath)

    # print(prpath, type(prpath), len(prpath))

    b["project"][f"{len(b['project'])}"] = {
            'name': [(a := pathProject.split("/"))[len(a)-1]][0],
            "path": prpath,
            "data_create": str(dt.now()).split(" ")[0]
        }
    path.write_text(json.dumps(b, indent=4), encoding='utf-8')



img = PhotoImage( file="refresh.png" )
img_trash = PhotoImage( file="trash_bin_icon-icons.com_67981.png" )
update_btn = Button( image=img, command=update )
delete_btn = Button( image=img_trash, command=delete )
open_btn = Button( text="Открыть", height=2, width=12, relief=RAISED,
    command=openproject )
loadfinishproject_btn = Button( text="Загрузить", height=2, width=12, relief=RAISED,
    command=loadFinishProject )

try:
    path = Path( 'result.json' )
    a = json.loads( path.read_text( encoding='utf-8' ) )
    names = list( a[ "names" ].keys() )
except:
    names = [ "Нет проектов" ]

lb.configure( yscrollcommand=sb.set )
sb.config( command=lb.yview )

for i in names:
    lb.insert( END, i )

sb.pack( fill=Y, side=RIGHT )
lb.pack( side=LEFT )
create_btn.place( x=300, y=5 )
update_btn.place( x=200, y=5 )
delete_btn.place( x=365, y=265 )
open_btn.place( x=300, y=50 )
loadfinishproject_btn.place( x=300, y=100 )


root.mainloop()
