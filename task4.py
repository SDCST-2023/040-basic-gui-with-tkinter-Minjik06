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
label1.place(x=60, y=0)
label2.place(x=130,y=40)
label3.place(x=0, y=100)
window.mainloop()