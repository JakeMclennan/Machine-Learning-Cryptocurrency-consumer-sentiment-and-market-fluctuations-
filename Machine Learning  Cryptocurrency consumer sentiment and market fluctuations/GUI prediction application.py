from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Day_Bitcoin_LR
import percent_up_down_bitcoin
import re
ret_type_1 = 0
ret_type_2 = 0
ret_type_3 = 0
ret_type_4 = 0
ret_type_5 = 0

def get_24():
    prediction_value()

def get_48():
    prediction_value_48()

def get_72():
    prediction_value_72()


def update_val():

    Label(root, text=var4.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=4, column=4)
    Label(root, text=var5.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=5, column=4)
    
    if (var1.get() == 0):
        Label(root, text=var1.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="black", height=1, width=4,).grid(row=1, column=4)
        Label(root, text=" Type 1: Government Regulation ", relief=RIDGE ,fg="black", font=("Helvetica", 9)).grid(row=1, column=3, padx=4,sticky=W)
    if (var1.get() == 1):
        Label(root, text=var1.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="green", height=1, width=4,).grid(row=1, column=4)
        Label(root, text=" Type 1: Government Regulation ", relief=RIDGE ,fg="green", font=("Helvetica", 9)).grid(row=1, column=3, padx=4,sticky=W)
    if (var1.get() == -1):
        Label(root, text=var1.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="red", height=1, width=4,).grid(row=1, column=4)
        Label(root, text=" Type 1: Government Regulation ", relief=RIDGE ,fg="red", font=("Helvetica", 9)).grid(row=1, column=3, padx=4,sticky=W)

    if (var2.get() == 0):
        Label(root, text=var2.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="black", height=1, width=4,).grid(row=2, column=4)
        Label(root, text=" Type 2: Security/Hacks ", relief=RIDGE ,fg="black", font=("Helvetica", 9)).grid(row=2, column=3, padx=4,sticky=W)
    if (var2.get() == 1):
        Label(root, text=var2.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="green", height=1, width=4,).grid(row=2, column=4)
        Label(root, text=" Type 2: Security/Hacks ", relief=RIDGE ,fg="green", font=("Helvetica", 9)).grid(row=2, column=3, padx=4,sticky=W)
    if (var2.get() == -1):
        Label(root, text=var2.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="red", height=1, width=4,).grid(row=2, column=4)
        Label(root, text=" Type 2: Security/Hacks ", relief=RIDGE ,fg="red", font=("Helvetica", 9)).grid(row=2, column=3, padx=4,sticky=W)

    if (var3.get() == 0):
        Label(root, text=var3.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="black", height=1, width=4,).grid(row=3, column=4)
        Label(root, text=" Type 3: Acceptance ", relief=RIDGE ,fg="black", font=("Helvetica", 9)).grid(row=3, column=3, padx=4,sticky=W)
    if (var3.get() == 1):
        Label(root, text=var3.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="green", height=1, width=4,).grid(row=3, column=4)
        Label(root, text=" Type 3: Acceptance ", relief=RIDGE ,fg="green", font=("Helvetica", 9)).grid(row=3, column=3, padx=4,sticky=W)
    if (var3.get() == -1):
        Label(root, text=var3.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="red", height=1, width=4,).grid(row=3, column=4)
        Label(root, text=" Type 3: Acceptance ", relief=RIDGE ,fg="red", font=("Helvetica", 9)).grid(row=3, column=3, padx=4,sticky=W)

    if (var4.get() == 0):
        Label(root, text=var4.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="black", height=1, width=4,).grid(row=4, column=4)
        Label(root, text=" Type 4: Opinion ", relief=RIDGE ,fg="black", font=("Helvetica", 9)).grid(row=4, column=3, padx=4,sticky=W)
    if (var4.get() == 1):
        Label(root, text=var4.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="green", height=1, width=4,).grid(row=4, column=4)
        Label(root, text=" Type 4: Opinion ", relief=RIDGE ,fg="green", font=("Helvetica", 9)).grid(row=4, column=3, padx=4,sticky=W)
    if (var4.get() == -1):
        Label(root, text=var4.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="red", height=1, width=4,).grid(row=4, column=4)
        Label(root, text=" Type 4: Opinion ", relief=RIDGE ,fg="red", font=("Helvetica", 9)).grid(row=4, column=3, padx=4,sticky=W)
        
    if (var5.get() == 0):
        Label(root, text=var5.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="black", height=1, width=4,).grid(row=5, column=4)
        Label(root, text=" Type 5: Changes to the block chain ", relief=RIDGE ,fg="black", font=("Helvetica", 9)).grid(row=5, column=3, padx=4,sticky=W)
    if (var5.get() == 1):
        Label(root, text=var5.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="green", height=1, width=4,).grid(row=5, column=4)
        Label(root, text=" Type 5: Changes to the block chain ", relief=RIDGE ,fg="green", font=("Helvetica", 9)).grid(row=5, column=3, padx=4,sticky=W)
    if (var5.get() == -1):
        Label(root, text=var5.get(), relief=SUNKEN,bg="floral white", font=("Helvetica", 10),fg="red", height=1, width=4,).grid(row=5, column=4)
        Label(root, text=" Type 5: Changes to the block chain ", relief=RIDGE ,fg="red", font=("Helvetica", 9)).grid(row=5, column=3, padx=4,sticky=W)
        



    

def get_accuracy_24():
    root.geometry("1050x220+100+100")
    Label(root, text="             ", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=8, padx=4)
    Label(root, text="24H Accuracy:", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=8, padx=4)
    Label(root, text=percent_up_down_bitcoin.type_correct(1), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=1, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct(2), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=2, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct(3), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=3, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct(4), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=4, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct(5), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=5, column=8)

def get_accuracy_48():
    root.geometry("1050x220+100+100")
    Label(root, text="             ", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=8, padx=4)
    Label(root, text="48H Accuracy:", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=8, padx=4)
    Label(root, text=percent_up_down_bitcoin.type_correct_48(1), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=1, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_48(2), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=2, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_48(3), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=3, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_48(4), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=4, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_48(5), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=5, column=8)

def get_accuracy_72():
    root.geometry("1050x220+100+100")
    Label(root, text="             ", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=8, padx=4)
    Label(root, text="72H Accuracy:", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=8, padx=4)
    Label(root, text=percent_up_down_bitcoin.type_correct_72(1), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=1, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_72(2), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=2, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_72(3), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=3, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_72(4), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=4, column=8)
    Label(root, text=percent_up_down_bitcoin.type_correct_72(5), relief=SUNKEN,bg="floral white", font=("Helvetica", 10), height=1, width=4,).grid(row=5, column=8)


def prediction_value():
    root.geometry("960x220+100+100")
    Theprediction = Day_Bitcoin_LR.UP_DOWN_24(var1.get(),var2.get(),var3.get(),var4.get(),var5.get())
    j = round((Theprediction * 100),4)
    pred = str(j)+"%"
    values = str("("+str(var1.get())+","+str(var2.get())+","+str(var3.get())+","+str(var4.get())+","+str(var5.get())+")")
 
    neg = round((100 - j),2);

    negative_pred = str(neg)+"%"
    theACCURACY = Button(root,text="Get 24H Accuracy:", command=get_accuracy_24)
    theACCURACY.grid(row=0,column=7)
    theACCURACY.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 8))
    
    if(j>0):
        Label(root, text=pred,bg="floral white", relief=SUNKEN,fg="green", font=("Helvetica", 14), height=1, width=10,).grid(row=1, column=7, padx=4),
        Label(root, text="                               ", relief=FLAT , font=("Helvetica", 10)).grid(row=1, column=6, padx=4)
        Label(root, text=" Model predicts price increase:", relief=FLAT , font=("Helvetica", 11)).grid(row=1, column=6, padx=4,)
    if(j<=0):
        Label(root, text=pred,bg="floral white", relief=SUNKEN,fg="red", font=("Helvetica", 14), height=1, width=10,).grid(row=1, column=7, padx=4),
        Label(root, text="                               ", relief=FLAT , font=("Helvetica", 10)).grid(row=1, column=6, padx=4)
        Label(root, text=" Model predicts price decrease:", relief=FLAT , font=("Helvetica", 11)).grid(row=1, column=6, padx=4)


def prediction_value_48():
    root.geometry("960x220+100+100")
    Theprediction = Day_Bitcoin_LR.UP_DOWN_48(var1.get(),var2.get(),var3.get(),var4.get(),var5.get())
    j = round((Theprediction * 100),4)
    pred = str(j)+"%"
    values = str("("+str(var1.get())+","+str(var2.get())+","+str(var3.get())+","+str(var4.get())+","+str(var5.get())+")")
    
    neg = round((100 - j),2);
    
    negative_pred = str(neg)+"%"

    theACCURACY = Button(root,text="Get 48H Accuracy:", command=get_accuracy_48)
    theACCURACY.grid(row=2,column=7)
    theACCURACY.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 8))
    if(j>0):
        Label(root, text=pred,bg="floral white", relief=SUNKEN,fg="green", font=("Helvetica", 14), height=1, width=10,).grid(row=3, column=7, padx=4),
        Label(root, text="                               ", relief=FLAT , font=("Helvetica", 10)).grid(row=3, column=6, padx=4)
        Label(root, text=" Model predicts price increase:", relief=FLAT , font=("Helvetica", 11)).grid(row=3, column=6, padx=4)
    if(j<=0):
        Label(root, text=pred,bg="floral white", relief=SUNKEN,fg="red", font=("Helvetica", 14), height=1, width=10,).grid(row=3, column=7, padx=4),
        Label(root, text="                               ", relief=FLAT , font=("Helvetica", 10)).grid(row=3, column=6, padx=4)
        Label(root, text=" Model predicts price decrease:", relief=FLAT , font=("Helvetica", 11)).grid(row=3, column=6, padx=4)

def prediction_value_72():
    root.geometry("960x220+100+100")
    Theprediction = Day_Bitcoin_LR.UP_DOWN_72(var1.get(),var2.get(),var3.get(),var4.get(),var5.get())
    j = round((Theprediction * 100),4)
    pred = str(j)+"%"
    values = str("("+str(var1.get())+","+str(var2.get())+","+str(var3.get())+","+str(var4.get())+","+str(var5.get())+")")
    neg = round((100 - j),2);

    negative_pred = str(neg)+"%"
    theACCURACY = Button(root,text="Get 72H Accuracy:", command=get_accuracy_72)
    theACCURACY.grid(row=4,column=7)
    theACCURACY.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 8))
    if(j>0):
        Label(root, text=pred,bg="floral white", relief=SUNKEN,fg="green", font=("Helvetica", 14), height=1, width=10,).grid(row=5, column=7, padx=4),
        Label(root, text="                               ", relief=FLAT , font=("Helvetica", 10)).grid(row=5, column=6, padx=4)
        Label(root, text=" Model predicts price increase:", relief=FLAT , font=("Helvetica", 11)).grid(row=5, column=6, padx=4)
    if(j<=0):
        Label(root, text=pred,bg="floral white", relief=SUNKEN,fg="red", font=("Helvetica", 14), height=1, width=10,).grid(row=5, column=7, padx=4),
        Label(root, text="                               ", relief=FLAT , font=("Helvetica", 10)).grid(row=5, column=6, padx=4)
        Label(root, text=" Model predicts price decrease:", relief=FLAT , font=("Helvetica", 11)).grid(row=5, column=6, padx=4)

root = Tk()


root.title("Bitcoin Price Fluctuation")
root.resizable(width=False, height=False)
style = ttk.Style()
ttk.Style().theme_use('vista')
style.configure("TButton", bg="black", font=("Helvetica", 8), relief="RAISED", activebackground="lavender")
#               width x height
root.geometry("800x220+100+100")
down_png = PhotoImage(file = 'down.png')
up_png = PhotoImage(file = 'up.png')
BTC_png = PhotoImage(file = 'Bitcoin135.png')
reset_png = PhotoImage(file = 'reset.png')


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

Label(root, text="Positive: 1", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=0, padx=4)
Label(root, text="Negative: -1", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=1, padx=4)
Label(root, text="Reset: 0", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=2, padx=4)
Label(root, text="Shock Inputs", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=4, padx=4)
Label(root, text="Shocks", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=3, padx=4)


Label(root, text="  Predict 24H  ", relief=FLAT , font=("Helvetica", 10)).grid(row=0, column=5, padx=4)
Label(root, text="  Predict 48H  ", relief=FLAT , font=("Helvetica", 10)).grid(row=2, column=5, padx=4)
Label(root, text="  Predict 72H  ", relief=FLAT , font=("Helvetica", 10)).grid(row=4, column=5, padx=4)



update_val()



#-----------Type 1----------
button1 = Radiobutton(root,image=up_png,fg="green",variable=var1, value=1, command=update_val)
button1.grid(row=1,column=0)
button1.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

button2 = Radiobutton(root,image=down_png,fg="red",variable=var1, value=-1, command=update_val)
button2.grid(row=1,column=1)
button2.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

reset1 = Radiobutton(root,image=reset_png,fg="blue",variable=var1, value=0, command=update_val)
reset1.grid(row=1,column=2)
reset1.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))
#-----------Type 2----------
button3 = Radiobutton(root,image=up_png,fg="green",variable=var2, value=1, command=update_val)
button3.grid(row=2,column=0)
button3.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

button4 = Radiobutton(root,image=down_png,fg="red",variable=var2, value=-1, command=update_val)
button4.grid(row=2,column=1)
button4.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

reset2 = Radiobutton(root,image=reset_png,fg="blue",variable=var2, value=0, command=update_val)
reset2.grid(row=2,column=2)
reset2.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))
#-----------Type 3----------
button5 = Radiobutton(root,image=up_png,fg="green",variable=var3, value=1, command=update_val)
button5.grid(row=3,column=0)
button5.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

button6 = Radiobutton(root,image=down_png,fg="red",variable=var3, value=-1, command=update_val) 
button6.grid(row=3,column=1)
button6.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

reset3 = Radiobutton(root,image=reset_png,fg="blue",variable=var3, value=0, command=update_val)
reset3.grid(row=3,column=2)
reset3.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))
#-----------Type 4----------
button7 = Radiobutton(root,image=up_png,fg="green",variable=var4, value=1, command=update_val)
button7.grid(row=4,column=0)
button7.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

button8 = Radiobutton(root,image=down_png,fg="red",variable=var4, value=-1, command=update_val)
button8.grid(row=4,column=1)
button8.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

reset4 = Radiobutton(root,image=reset_png,fg="blue",variable=var4, value=0, command=update_val)
reset4.grid(row=4,column=2)
reset4.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))
#-----------Type 5----------
button9 = Radiobutton(root,image=up_png,fg="green",variable=var5, value=1, command=update_val)
button9.grid(row=5,column=0)
button9.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

button10 = Radiobutton(root,image=down_png,fg="red",variable=var5, value=-1, command=update_val)
button10.grid(row=5,column=1)
button10.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

reset5 = Radiobutton(root,image=reset_png,fg="blue",variable=var5, value=0, command=update_val)
reset5.grid(row=5,column=2)
reset5.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

#--------- Prediction ------- Button
thebutton = Button(root,image=BTC_png, command=get_24)
thebutton.grid(row=1,column=5)
thebutton.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

thebutton = Button(root,image=BTC_png, command=get_48)
thebutton.grid(row=3,column=5)
thebutton.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))

thebutton = Button(root,image=BTC_png, command=get_72)
thebutton.grid(row=5,column=5)
thebutton.config(activebackground="lavender",activeforeground="lavender", compound=LEFT, font=("Helvetica", 12))




root.mainloop()


