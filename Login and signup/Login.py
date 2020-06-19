from tkinter import *
scr=Tk(className="Log in")

u=Label(scr,text='UserName',font=('times',15,'bold'))
u.grid(row=1,column=0)
ue=Entry(scr,font=('times',15,))
ue.grid(row=1,column=1)

p=Label(scr,text='Password',font=('times',15,'bold'))
p.grid(row=2,column=0)
pe=Entry(scr,font=('times',15))
pe.grid(row=2,column=1)

message=Label(scr,font=('times',15,'italic'),text='')
message.grid(row=4,column=0)

def search():
    lines=open('database.txt','r').readlines()
    for i in lines:
        if ue.get()==i.split()[0] and pe.get()==i.split()[1]:
            message.config(text='Successfully Logged in')
            break
        else:
            message.config(text='invalid username or password')

def fun():
    if re.search(r'^\S+$',ue.get()) and re.search(r'^\S+$',pe.get()):
        search()
    else:
        message.config(text='Space not allowed in username or password')

b=Button(scr,text='Login',font=('times',15,'bold'),command=fun)
b.grid(row=4,column=1)





