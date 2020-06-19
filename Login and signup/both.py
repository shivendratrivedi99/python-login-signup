from tkinter import *
scr=Tk(className="Login or Signup")

def login():
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

    def search1():
        lines=open('database.txt','r').readlines()
        for i in lines:
            if ue.get()==i.split()[0] and pe.get()==i.split()[1]:
                message.config(text='Successfully Logged in')
                break
            else:
                message.config(text='invalid username or password')

    def fun():
        if re.search(r'^\S+$',ue.get()) and re.search(r'^\S+$',pe.get()):
            search1()
        else:
            message.config(text='Space not allowed in username or password')

    b=Button(scr,text='Login',font=('times',15,'bold'),command=fun)
    b.grid(row=4,column=1)


def signup():
    u=Label(scr,text='UserName',font=('times',15,'bold'))
    u.grid(row=1,column=0)
    ue=Entry(scr,font=('times',15,))
    ue.grid(row=1,column=1)

    p=Label(scr,text='Password',font=('times',15,'bold'))
    p.grid(row=2,column=0)
    pe=Entry(scr,font=('times',15))
    pe.grid(row=2,column=1)

    rp=Label(scr,text='Retype Password',font=('times',15,'bold'))
    rp.grid(row=3,column=0)
    rpe=Entry(scr,font=('times',15))
    rpe.grid(row=3,column=1)

    message=Label(scr,font=('times',15,'italic'),text='')
    message.grid(row=4,column=0)

    def search(x,y):
        lines=open('database.txt','r').readlines()
        for i in lines:
            if x==i.split()[0] and y==i.split()[1]:
                return 1
        return 0


    def fun():
        if re.search(r'^\S+$',ue.get()) and re.search(r'^\S+$',pe.get()):
            if rpe.get()==pe.get():
                message.config(text='Successfully signed up')
                if(search(ue.get(),pe.get())):
                    message.config(text='already exists kindly login')
                else:
                    file=open('database.txt','a+')
                    file.write(ue.get()+" "+pe.get()+"\n")
                
            else:
                message.config(text='password mismatch')
        else:
            message.config(text='Space not allowed in username or password')

    b=Button(scr,text='Register',font=('times',15,'bold'),command=fun)
    b.grid(row=4,column=1)

b=Button(scr,text='Login',font=('times',15,'bold'),command=login)
b.grid(row=1,column=1)
b=Button(scr,text='Signup',font=('times',15,'bold'),command=signup)
b.grid(row=2,column=1)








