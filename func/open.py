from tkinter import *


def openp():
    root = Tk()
    root.title("Информация о проекте")
    root.geometry(f"{400}x{300}")
    count = 0
    path = Path('result.json')
    b = json.loads(path.read_text(encoding='utf-8'))
    a = lb.curselection()



    info = {
        "name": b["project"][f"{a[0]}"]["name"],
        "path": b["project"][f"{a[0]}"]["path"],
        "to_create": b["project"][f"{a[0]}"]["data_create"]
    }
    lab_info = [
        Label(root, text=f'Имя: {info["name"]}', font=font),
        Label(root, text=f'Путь: {info["path"]}', font=font),
        Label(root, text=f'Дата создания: {info["to_create"]}', font=font)
    ]
    # var = {
    #     "vsCode" : IntVar(),
    #     "pyCharm" :  IntVar(),
    #     "explorer" : IntVar()
    # }
    it = IntVar()
    @ds
    class sel:
        vsCode: bool= False
        pycharm: bool= False
        explorer: bool= False
    s = sel()
    def select():
        h = it.get()
        print(h)
        if h == 1:
            s.vsCode = True
        if h == 2:
            s.pycharm = True
        if h == 3:
            s.explorer = True



    # cl = onclick(count)
    chkValue = tk.BooleanVar()

    e = tk.Checkbutton(root, text='Check Box',
                            variable=chkValue)


    # command_check = {
    #     "vsCode": lambda : g.click(var["vsCode"]),
    #     "pyCharm": lambda : g.click(var["pyCharm"]),
    #     "explorer": lambda : g.click(var["explorer"]),
    # }

    def ok():
        print("----------------")
        print(chkValue.get())
        # print(s)
        # print(s)

        # if var["vsCode"].get() == 1:
        #     os.system("code .")
        # if var["pyCharm"].get() == 1:
        #     os.system("pycharm .")
        # if var["explorer"].get() == 1:
        #     os.system("start .")
        # time.sleep(1)
        # var["vsCode"].set(0)
        # var["pyCharm"].set(0)
        # var["explorer"].set(0)
        # time.sleep(1)

        # root.destroy()



    btn = Button(root, text="Ok", font=font, width=10, command=ok)

    lab_info[0].place(x=1, y=1)
    lab_info[1].place(x=1, y=30)
    lab_info[2].place(x=1, y=60)
    e.grid(column=0, row=0)
    # vs.place(x=1, y=100)
    # py.place(x=105, y=100)
    # ex.place(x=230, y=100)



    btn.place(x=0, y=150)


    root.mainloop()