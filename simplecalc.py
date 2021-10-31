from tkinter import *
root=Tk()
root.title('Simple Calculater')

myentry=Entry(root,width=60,borderwidth=5)
myentry.grid(row=1,column=0,ipadx=68,ipady=20,columnspan=3)

def add():
    global fn
    global math
    fn=myentry.get()
    fn=int(fn)
    
    math='addition'
    myentry.delete(0,END)
    
    sn=myentry.get()

def sub():
    global fn
    global math
    fn=myentry.get()
    fn=int(fn)
    
    math='sub'
    myentry.delete(0,END)
    
    sn=myentry.get()

def mul():
    global fn
    global math
    fn=myentry.get()
    fn=int(fn)
    
    math='mul'
    myentry.delete(0,END)
    
    sn=myentry.get()

def div():
    global fn
    global math
    fn=myentry.get()
    fn=int(fn)
    
    math='div'
    myentry.delete(0,END)
    
    sn=myentry.get()
        
def button_click(num):
    current=myentry.get()
    myentry.delete(0,END)
    myentry.insert(0,str(current)+str(num))

def button_clear():
    myentry.delete(0,END)

def bteql():
    sn=myentry.get()
    myentry.delete(0,END)
    if math=='addition':
        myentry.insert(0,fn+int(sn))
    if math=='sub':
        myentry.insert(0,fn-int(sn))
    if math=='mul':
        myentry.insert(0,fn*int(sn))
    if math=='div':
        if int(sn)==0:
            myentry.insert(0,'Error...!')
        else:
            myentry.insert(0,fn/int(sn))
    



btn1=Button(root,text="1",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(1))
btn2=Button(root,text="2",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(2))
btn3=Button(root,text="3",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(3))

btn4=Button(root,text="4",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(4))
btn5=Button(root,text="5",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(5))
btn6=Button(root,text="6",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(6))

btn7=Button(root,text="7",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(7))
btn8=Button(root,text="8",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(8))
btn9=Button(root,text="9",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(9))

btn0=Button(root,text="0",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=lambda:button_click(0))

btn_clr=Button(root,text="C",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=button_clear)
btn_add=Button(root,text="+",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=add)
btn_sub=Button(root,text="-",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=sub)

btn_mul=Button(root,text="*",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=mul)
btn_div=Button(root,text="/",width=20,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=div)
btn_eql=Button(root,text="=",width=66,height=5,bg="gray",padx=10,pady=10,font=("times new roman",12,"bold"),command=bteql)

btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
               
btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
               
btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)

btn_clr.grid(row=5,column=0)
btn0.grid(row=5,column=1)
btn_add.grid(row=5,column=2)




btn_sub.grid(row=6,column=1)
btn_mul.grid(row=6,column=0)
btn_div.grid(row=6,column=2)

btn_eql.grid(row=7,column=0,columnspan=3)

mainloop()
