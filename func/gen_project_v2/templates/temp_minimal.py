import os
from tkinter import messagebox as mb


main =\
"""
print("Hello, World")


if __name__ == "__main__"
    pass

"""





def minimal(path, n, lab):
    if not os.path.exists(f"{path}/{n}") and n is not None:
        project = f"{path}/{n}/"
        os.mkdir(project)
        os.system(f"echo > {project}main.py")

        with open(f"{project}main.py", "w") as file:
            file.write(main)

        if os.system(f"pycharm {path}/{n}") == 1:
                os.system(f"code {path}/{n}")

        lab.config(text=f'проект создан по пути: {path}')
        mb.showinfo(message=f'проект создан по пути: {path}')

        os.system(f"start {project}")
    else:
        lab.config(text=f'Такая папка уже существует или вы не указали имя папки')




