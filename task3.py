import tkinter as tk
from tkinter.constants import RIGHT, TOP 
import pyautogui as p

window = tk.Tk()
window.title("Example")
window.geometry("260x135")
text=tk.StringVar()

dogphoto = tk.PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window,text="Pochacco!")
label3 = tk.Label(window, text="Acuddlu little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", bg="#A3FFFF")
label1.grid(row=0, rowspan=1, column=3)
label2.grid(row=0, rowspan=1, column=4)
label3.grid(row=2, column=0, columnspan=8)

window.mainloop()

