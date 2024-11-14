import tkinter as tk
import math
import array

root = tk.Tk()
res3 = []
root.title("Hello app")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 550
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Функции
def summ():
    sum = (int(entry1.get())+int(entry2.get())+int(entry3.get())+int(entry4.get()))
    label1.config (text=sum)
def proizv():
    proiz = (int(entry1.get())*int(entry2.get())*int(entry3.get())*int(entry4.get()))
    label1.config (text=proiz)
def maxim():
    res2 = [int(entry1.get()),int(entry2.get()),int(entry3.get()),int(entry4.get())]
    res3=res2
    maxb=max(res3)
    label1.config (text=maxb)
def minim():
    res2 = [int(entry1.get()),int(entry2.get()),int(entry3.get()),int(entry4.get())]
    res3=res2
    maxb=min(res3)
    label1.config (text=maxb)

#Кнопки
button1 = tk.Button(root, text="Сумма", command=summ)
button1.place(x=100, y=120)

button2 = tk.Button(root, text="Произведение", command=proizv)  
button2.place(x=100, y=180)

button3 = tk.Button(root, text="Максимум", command=maxim)
button3.place(x=100, y=240)

button4 = tk.Button(root, text="Минимум", command=minim)
button4.place(x=100, y=300)

#Ввод

entry1= tk.Entry(root)
entry1.place(x=230, y=120)

entry2= tk.Entry(root)
entry2.place(x=230, y=180)

entry3= tk.Entry(root)
entry3.place(x=230, y=240)

entry4= tk.Entry(root)
entry4.place(x=230, y=300)

#Вывод
label1 = tk.Label(root)
label1.place(x=450, y=200)


root.mainloop()