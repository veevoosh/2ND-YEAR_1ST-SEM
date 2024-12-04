from tkinter import *
from functools import partial
win = Tk()
res = Label(win, width=23, text="0", bg="black", fg="lightgreen", font=("Arial", 18), anchor="e")  #Anchor for text positioning (EAST) thank u bekah >:3
res.grid(row=0, column=0, columnspan=4)
btn_txt = ["**", "//", "%", "C", "7", "8", "9", "-", "4", "5", "6", "+", "1", "2", "3", "/", "0", ".", "=", "*"]
row_num, col_num = 0, 0
def input_value(text):  #Thank you so much Marj!!! >:3c
    current_text = res.cget("text")
    if text == "C": res.config(text="0")  #Clear current text
    elif text == "=":
        try:
            result = str(eval(current_text))  #Evaluate and compute operations
            res.config(text=result)  #Display result of computation...
        except:
            res.config(text="Error")  #...Otherwise, Error!
    else:
        if current_text == "0" or current_text == "Error": current_text = ""  #Replace current text after display
        res.config(text=current_text + str(text))  #Concatenate text from button input
for i in range(len(btn_txt)):
    Button(win, width=5, text=btn_txt[i], font=("Arial", 18), cursor="hand2", command=partial(input_value, btn_txt[i])).grid(row=row_num + 1, column=col_num)
    col_num += 1
    if col_num == 4:
        row_num += 1
        col_num = 0
win.title("Domingo - Calculator v2")
win.geometry("328x265+800+415")
win.config(bg="#996699")
win.mainloop()