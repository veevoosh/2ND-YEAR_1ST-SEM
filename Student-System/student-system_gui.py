from tkinter import *
from functools import partial

win = Tk()
win.title("Domingo - Student System GUI v1")
win.geometry(f"1280x800+{(win.winfo_screenwidth()-1280)//2}+{(win.winfo_screenheight()-800)//2}")

def content1_button():
    cont1_div.pack(side="left", fill="x")
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    cont_div.pack_forget()  #to get rid of "Press Buttons To See Text Here!" overlay

def content2_button():
    cont2_div.pack(side="left", fill="x")
    cont1_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    cont_div.pack_forget()

def content3_button():
    cont3_div.pack(side="left", fill="x")
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    cont_div.pack_forget()

def content3_button():
    cont3_div.pack(side="left", fill="x")
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    cont_div.pack_forget()

def content4_button():
    cont4_div.pack(side="left", fill="x")
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont5_div.pack_forget()
    cont_div.pack_forget()

def content5_button():
    cont5_div.pack(side="left", fill="x")
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont_div.pack_forget()

btns = []
btn_txt = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
func = [content1_button, content2_button, content3_button, content4_button, content5_button]

#overall body

main_div = Frame(win, bg="white")
main_div.pack(side="left", fill="both", expand=True)

#menu div

menu_div = Frame(main_div, bg="#996699")
menu_div.pack(side="left", fill="y")

#content div

cont_div = Frame(main_div, bg="white")  #temp overlay to hide option texts
cont_div.pack(side="left", fill="x")
Label(cont_div, width=95, text="Press Buttons To See Text Here!", font=("Courier New", 14), pady=15).grid(row=0, column=0)

cont1_div = Frame(main_div, bg="black")
cont1_div.pack(side="left", fill="x")
Label(cont1_div, width=95, text=">> Option 1 Pressed", font=("Courier New", 14), pady=15).grid(row=0, column=0)

cont2_div = Frame(main_div, bg="black")
cont2_div.pack(side="left", fill="x")
Label(cont2_div, width=95, text=">> Option 2 Pressed", font=("Courier New", 14), pady=15).grid(row=0, column=0)

cont3_div = Frame(main_div, bg="black")
cont3_div.pack(side="left", fill="x")
Label(cont3_div, width=95, text=">> Option 3 Pressed", font=("Courier New", 14), pady=15).grid(row=0, column=0)

cont4_div = Frame(main_div, bg="black")
cont4_div.pack(side="left", fill="x")
Label(cont4_div, width=95, text=">> Option 4 Pressed", font=("Courier New", 14), pady=15).grid(row=0, column=0)

cont5_div = Frame(main_div, bg="black")
cont5_div.pack(side="left", fill="x")
Label(cont5_div, width=95, text=">> Option 5 Pressed", font=("Courier New", 14), pady=15).grid(row=0, column=0)

for i in range(len(btn_txt)):
    btns.append(Button(menu_div, anchor="e", bg="#FFFFFF", text=btn_txt[i], width=21, font=("Courier New", 14), padx=10, pady=15))

for i in range(len(btns)):
    btns[i].grid(row=i+1, column=0)

    for i in range(len(func)):
        btns[i].config(command=func[i])

#label

Label(menu_div, width=23, text="Main Menu", font=("Courier New", 14), pady=15).grid(row=0, column=0)  #courier new is a nice font

win.mainloop()