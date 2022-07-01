# from tkinter import *
#
# top = Tk()
# sb = Scrollbar(top)
# sb.pack(side = RIGHT, fill = Y)
#
# mylist = Listbox(top, yscrollcommand = sb.set )
#
#
#
# for line in range(1, 31):
#     mylist.insert(END, "Number " + str(line))
#
# mylist.pack( side = LEFT )
# sb.config( command = mylist.yview )


# mainloop()


# from tkinter import *
# #
# #
# # ws = Tk()
# # ws.title( 'PythonGuides' )
# # ws.geometry( '400x300' )
# # # ws.config(bg='#4A7A8C')
# # a = [ "sad", "sdad", "r3" ]
# # frame = Frame( ws, height=300 )
# # frame.place( x=1, y=1 )
# #
# # lb = Listbox( frame, font=12, height=15, listvariable=a )
# #
# # sb = Scrollbar( frame, orient=VERTICAL )
# #
# # lb.configure( yscrollcommand=sb.set )
# # sb.config( command=lb.yview )
# #
# # sb.pack( fill=Y, side=RIGHT )
# # lb.pack( side=LEFT )
# #
# # for i in a:
# #     lb.insert( END, i )
# #
# # ws.mainloop()
# import json
#

#
#
# import json
# from pathlib import Path
#
# path = Path('result.json')
#
# data = json.loads(path.read_text(encoding='utf-8'))
#
# data[len(data)-1]["project"] = {'timestamp':0.015,'movement':'type_2'}
#
# path.write_text(json.dumps(data, indent=4), encoding='utf-8')


from tkinter import *

def sel():
  selection = "Вы выбрали " + str(var.get())
  label.config(text = selection)

root = Tk()
root.title("Пример работы радио-кнопок")
root.minsize(width=500, height=400)

# создаем радио-кнопки используя переменную-объект типа IntVar()
var = IntVar()
R1 = Radiobutton(root, text="Windows", variable=var, value=1, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Linux", variable=var, value=2, command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="MacOS", variable=var, value=3, command=sel)
R3.pack( anchor = W )

label = Label(root)
label.pack()

# запускаем программу
root.mainloop()