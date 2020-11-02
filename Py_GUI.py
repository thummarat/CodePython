from tkinter import *
from tkinter import ttk
mainFrm = Tk()
mainFrm.title("การสร้าง GUI ด้วย tkinter")
lbTitle = ttk.Label(mainFrm, text="บวกเลข", font="20")

lbTitle.grid(column=0, columnspan=2, padx=150, pady=10)
mainFrm.mainloop()