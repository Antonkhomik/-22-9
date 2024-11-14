import tkinter as tk

from tkinter import PhotoImage

root = tk.Tk()
#Лого
icon = tk.PhotoImage(file="sport.png")
root.iconphoto(root, icon)

root.title("Триатлон")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 550
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
#Функции
def count():
   res1 = (int(entry1.get())+int(entry4.get())+int(entry7.get()))
   vivod1.config (text=res1)

   res2 = (int(entry2.get())+int(entry5.get())+int(entry8.get()))
   vivod2.config (text=res2)   

   res3 = (int(entry3.get())+int(entry6.get())+int(entry9.get()))
   vivod3.config (text=res3)


   
#Текст
label1 = tk.Label(root, text="триатлон")
label1.place(x=450, y=1)

label2 = tk.Label(root, text="Время")
label2.place(x=230, y=100)

label3 = tk.Label(root, text="игрок 1")
label3.place(x=310, y=100)

label4 = tk.Label(root, text="игрок 2")
label4.place(x=380, y=100)

label5 = tk.Label(root, text="игрок 3")
label5.place(x=460, y=100)

label6 = tk.Label(root, text="самбо")
label6.place(x=230, y=140)

label7 = tk.Label(root, text="каратэ")
label7.place(x=230, y=180)

label8 = tk.Label(root, text="дзюдо")
label8.place(x=230, y=220)

label9 = tk.Label(root, text="число побед:")
label9.place(x=230, y=260)

vivod1= tk.Label(root)
vivod1.place(x=310, y=260)

vivod2= tk.Label(root)
vivod2.place(x=390, y=260)

vivod3= tk.Label(root)
vivod3.place(x=440, y=260)

#ввод данных

entry1= tk.Entry(root)
entry1.place(x=310, y=140)

entry2= tk.Entry(root)
entry2.place(x=390, y=140)

entry3= tk.Entry(root)
entry3.place(x=440, y=140)

entry4= tk.Entry(root)
entry4.place(x=310, y=180)

entry5= tk.Entry(root)
entry5.place(x=390, y=180)

entry6= tk.Entry(root)
entry6.place(x=440, y=180)

entry7= tk.Entry(root)
entry7.place(x=310, y=220)

entry8= tk.Entry(root)
entry8.place(x=390, y=220)

entry9= tk.Entry(root)
entry9.place(x=440, y=220)

#Кнопки
button1 = tk.Button(root, text="Расчет времени", command=count)
button1.place(x=510, y=420)

#изображение
image = PhotoImage(file="sport.png")
image_label = tk.Label(root, image=image)
image_label.place(x=5, y=5)

root.mainloop()