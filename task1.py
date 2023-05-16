import tkinter as tk 


window = tk.Tk()
window.title("tk")
window.geometry("437x30")
text=tk.StringVar()

label1 = tk.Entry(window, textvariable=text)
label2 = tk.Label(window, text="x")
label3 = tk.Entry(window, textvariable=text)
button1 = tk.Button(window,text="=")
label4 = tk.Entry(window, textvariable=text)

label1.grid(row = 0, column = 0, padx=3)
label2.grid(row=0, column=1 , padx=3)
label3.grid(row=0, column=2, padx=3)
button1.grid(row=0, column=3, padx=3)
label4.grid(row=0, column=4)
window.mainloop()


"""entry1 = tk.Label(window,text="=")"""