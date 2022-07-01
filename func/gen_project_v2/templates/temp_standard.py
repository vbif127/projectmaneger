import os
from tkinter import messagebox as mb
test = """import unittest
    

class MyTestCase( unittest.TestCase ):


    def test_something( self ):
        self.assertEqual( True, False )  # add assertion here


if __name__ == '__main__':
    unittest.main()
"""
imports = """
import os, sys
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath(".."))
"""





def standard(path, n, lab):
    if not os.path.exists(f"{path}/{n}") and n is not None:
        lab.config(text=f'проект создан по пути: {path}')
        mb.showinfo(message=f'проект создан по пути: {path}')

        # /create folder
        os.mkdir( f"{path}/{n}" )
        os.mkdir( f"{path}/{n}/server" )
        os.mkdir( f"{path}/{n}/test" )
        os.mkdir( f"{path}/{n}/client" )

        # /create file
            # /test
        os.system( f"echo > {path}/{n}/test/tests.py" )
        os.system( f"echo > {path}/{n}/test/__init__.py" )

            # /server
        os.system( f"echo > {path}/{n}/server/backend.py" )
        os.system( f"echo > {path}/{n}/server/__init__.py" )
        os.system( f"echo > {path}/{n}/server/imports.py" )

            # /client
        os.system( f"echo > {path}/{n}/client/frontend.py" )
        os.system( f"echo > {path}/{n}/client/imports.py" )

            # /other
        os.system( f"echo > {path}/{n}/run.cmd" )
        os.system( f"echo > {path}/{n}/requirements.txt" )
        os.system( f"echo > {path}/{n}/.gitignore")

        # writing to a file
            # /test
        with open( f"{path}/{n}/test/tests.py", "w" ) as file:
            file.write( test )

        with open( f"{path}/{n}/test/__init__.py", "w" ) as file:
            file.write( "from . import *" )

            # /server
        with open( f"{path}/{n}/server/__init__.py", "w" ) as file:
            file.write( "from . import *" )

        with open( f"{path}/{n}/server/backend.py", "w" ) as file:
            file.write( "from .imports import * \n\n" )
            file.write( "class Backend:\n\tpass" )

        with open( f"{path}/{n}/server/imports.py", "w" ) as file:
            file.write( "# This file is for all import" )

            # /client
        with open( f"{path}/{n}/client/frontend.py", "w" ) as file:
            file.write( "from imports import * \n\n" )
            file.write( "class Frontend:\n\tpass\ninput()" )

        with open( f"{path}/{n}/client/imports.py", "w" ) as file:
            file.write( "# This file is for all import" )
            file.write(imports)

            # /other
        with open( f"{path}/{n}/run.cmd", "w" ) as file:
            file.write( f"cls\npy %cd%\\client\\frontend.py" )

        if os.path.abspath( ".." ) == "C:\\Users\\mihac\\gen_project":
            with open( "{path}/.gitignore", "w" ) as file:
                file.write( f"{path}/{n}" )

        if os.system(f"pycharm {path}/{n}") == 1:
            os.system(f"code {path}/{n}")

        os.system(f"start {path}/{n}")

    else:
        lab.config(text=f'Такая папка уже существует или вы не указали имя папки')
        # print("Такая папка уже существует или вы не указали имя папки")