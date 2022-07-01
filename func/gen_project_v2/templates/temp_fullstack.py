import os
from tkinter import  messagebox as mb


imports = """
import os, sys
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath(".."))
"""
def fullstack(path, n, lab):

    project = f"{path}/{n}"
    if not os.path.exists(f"{project}") and n is not None:
        lab.config(text=f'проект создан по пути: {path}')
        mb.showinfo(message=f'проект создан по пути: {path}')

        # /create folder
        os.mkdir( f"{project}" )
        os.mkdir( f"{project}/server" )
        os.mkdir( f"{project}/client" )

        # /create file
            # /server
        os.system( f"echo > {project}/server/backend.py" )
        os.system( f"echo > {project}/server/__init__.py" )
        os.system( f"echo > {project}/server/imports.py" )

            # /client
        os.system( f"echo > {project}/client/frontend.py" )
        os.system( f"echo > {project}/client/imports.py" )

            # /other
        os.system( f"echo > {project}/run.cmd" )
        os.system( f"echo > {project}/requirements.txt" )
        os.system( f"echo > {project}/.gitignore")

        # writing to a file
            # /server
        with open( f"{project}/server/__init__.py", "w" ) as file:
            file.write( "from . import *" )

        with open( f"{project}/server/backend.py", "w" ) as file:
            file.write( "from .imports import * \n\n" )
            file.write( "class Backend:\n\tpass" )

        with open( f"{project}/server/imports.py", "w" ) as file:
            file.write( "# This file is for all import" )

            # /client
        with open( f"{project}/client/frontend.py", "w" ) as file:
            file.write( "from imports import * \n\n" )
            file.write( "class Frontend:\n\tpass\ninput()" )

        with open( f"{project}/client/imports.py", "w" ) as file:
            file.write( "# This file is for all import" )
            file.write(imports)

            # /other
        with open( f"{project}/run.cmd", "w" ) as file:
            file.write( f"cls\npy %cd%\\client\\frontend.py" )

        if os.path.abspath( ".." ) == "C:\\Users\\mihac\\gen_project":
            with open( "{path}/.gitignore", "w" ) as file:
                file.write( f"{project}" )

        if os.system(f"pycharm {project}") == 1:
            os.system(f"code {project}")

        os.system(f"start {project}")

    else:
        lab.config(text=f'Такая папка уже существует или вы не указали имя папки')






