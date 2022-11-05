from tkinter import *  
root = Tk()  
root.geometry("500x500") 
root.title('ListBox')
root.config(bg='grey') 
  
lb1= Label(root, text="First Name", width=10, font=("arial",12))  
lb1.place(x=20, y=120)  
en1= Entry(root)  
en1.place(x=200, y=120)  
  
lb3= Label(root, text="Last Name", width=10, font=("arial",12))  
lb3.place(x=19, y=160)  
en3= Entry(root)  
en3.place(x=200, y=160)

lb4= Label(root, text="Email", width=10, font=("arial",12))  
lb4.place(x=25, y=200)  
en4= Entry(root)  
en4.place(x=220, y=200) 
  
lb5= Label(root, text="Gender", width=15, font=("arial",12))  
lb5.place(x=10, y=240)  
vars = IntVar()  
Radiobutton(root, text="Male", padx=5,variable=vars, value=1).place(x=180, y=240)  
Radiobutton(root, text="Female", padx =10,variable=vars, value=2).place(x=240,y=240)

lb6= Label(root, text="Languages", width=20, font=("arial",12))
lb6.place(x=10, y=280)
vars = IntVar()
Radiobutton(root, text="English", padx=15,variable=vars, value=1).place(x=210, y=280)
Radiobutton(root, text="Hindi", padx=20,variable=vars, value=2).place(x=280, y=280)

list_of_cntry = ("United States", "India", "Nepal", "Germany")  
cv = StringVar()  
drplist= OptionMenu(root, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set("Choose State")  
lb2= Label(root, text="State", width=13,font=("arial",12))  
lb2.place(x=20,y=350)  
drplist.place(x=300, y=350)

lb7= Label(root, text="Zip", width=10, font=("arial",12))  
lb7.place(x=50, y=390)  
en7= Entry(root)  
en7.place(x=250, y=390) 

lb8= Label(root, text="Credit Card Type", width=20, font=("arial",12))  
lb8.place(x=80, y=420)  
en8= Entry(root)  
en8.place(x=302, y=430)

lb9= Label(root, text="Address", width=10, font=("arial",12))  
lb9.place(x=100, y=470)  
en9= Entry(root)  
en9.place(x=310, y=470)   

 
root.mainloop()