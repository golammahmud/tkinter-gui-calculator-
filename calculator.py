from tkinter import *

root=Tk(className="Calculator")
root.geometry('300x350')

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue ,font='lucida 20 bold italic',justify='left')
screen.pack(fill=X,ipady=15)

f=Frame(root,)
f.pack()

def click(event):
    text=event.widget.cget('text')
    value=scvalue.get()
    if text  == '=':
        if value.isdigit():
            value=int(value)
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update
    
    elif text == 'c':
        scvalue.set("")
        screen.update()
        
    
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()
    
    
    
    
    
b=Button(f,text='9',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,fill='both')
b.bind("<Button-1>",click)
b=Button(f,text='8',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='7',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='/',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,)
b.bind("<Button-1>",click)


f=Frame(root,)
f.pack()
b=Button(f,text='6',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='5',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='4',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='*',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,)
b.bind("<Button-1>",click)


f=Frame(root,)
f.pack()
b=Button(f,text='3',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='2',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='1',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='+',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,)
b.bind("<Button-1>",click)


f=Frame(root,)
f.pack()

b=Button(f,text='c',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='0',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='=',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)
b=Button(f,text='-',font='lucida 20 bold italic',padx=6,pady=4)
b.pack(side=LEFT,padx=10,pady=10,)
b.bind("<Button-1>",click)



# # buttons
# buttons = ['9','8','7','/','6','5','4',"*",'3','2','1','+','.','0','=','-',]

# # counter
# count = 0

# for i in  range(1,5):
#     for j in range(4):
#         b=Button(f,text=buttons[count],font='lucida 20 bold italic').grid(row=i,column=j)
#         count+=1
  

root.mainloop()
 