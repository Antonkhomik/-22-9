import tkinter as tk
import math

root = tk.Tk()
root.title("Hello app")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 550
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

def plusik():
    sum = (int(entry1.get())+int(entry2.get())+50)
    answer.config (text=sum)
def minusik():
    minus = (int(entry1.get())-int(entry2.get()))
    answer.config (text=minus)
def multip():
    mult = (int(entry1.get())*int(entry2.get()))
    answer.config (text=mult)
def divis():
    div = (int(entry1.get())/int(entry2.get())/2)
    answer.config (text=div)
def power():
    pows = pow(int(entry1.get()), int(entry2.get()))
    answer.config (text=pows)
def sqrten():
    sqrts = float(answer.get())
    res = math.sqrt(sqrts)
    answer.config(text=res)
def clear():
    answer.delete
    entry1.delete
    entry2.delete

plusik=tk.Button(root, text="+", command=plusik)
plusik.place(x=140,y=260)
minusik=tk.Button(root, text="-", command=minusik)
minusik.place(x=140, y=290)
multip=tk.Button(root, text="*", command=multip)
multip.place(x=160,y=290)
divis=tk.Button(root, text="/", command=divis)
divis.place(x=160, y=260)
power=tk.Button(root, text="^", command=power)
power.place(x=140, y=230)
sqrten=tk.Button(root, text="√", command=sqrten)
sqrten.place(x=160, y=230)
deleteall=tk.Button(root, text="DEL", command=clear)
deleteall.place(x=180, y=260)

entry1=tk.Entry(root)
entry1.place(x=130, y=100)
entry2=tk.Entry(root)
entry2.place(x=130, y=130)

answer=tk.Label(root)
answer.place(x=450, y=5)
root.mainloop()
