from tkinter import *
import sqlite3 as sql
import re
from tkinter import messagebox
import requests as r
import bs4
import _thread

class Gui:
    def __init__(s):
        s.client=sql.connect('user.db')
        s.cu=s.client.cursor()
        try:
            s.cu.execute("create table user(id int auto_increment,name varchar(50),password varchar(20),email varchar(100))")
        except:
            pass
        s.scrap()
    def display(s,le,na,pr):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1366x600+0+0')#'widthxheight+x+y
        s.scr.config(bg='white')
        w = Scrollbar(s.scr)
        w.pack(side=RIGHT)
        l=Label(s.scr,bg='blue',font=('times',30,'bold'),text='Results')
        l.pack(side=TOP,fill=X)
        
        for i in range(le):
            j=0
            l=Label(s.scr,bg='thistle1',font=('times',30,'italic'),text=na[i])
            l.place(x=(50),y=(100+i*50))
            
            l=Label(s.scr,bg='thistle1',font=('times',30,'italic'),text=pr[i])
            l.place(x=(1150),y=(100+i*50))

        s.scr.mainloop()

    def name1(s,s1,name):
        print(1)
        for i in s1.findAll('div',{'class':'style__pro-title___3G3rr'}):
            name.append(i.text)
    def price1(s,s1,price):
        print(2)
        for i in s1.findAll('div',{'class':'style__price-tag___KzOkY'}):
            price.append(i.text)
        
        
    def search(s,query):
        str="https://www.1mg.com/search/all?name='"+query+"'"
        data=r.request('get',str)
        s1=bs4.BeautifulSoup(data.text,'html.parser')
        name=[]
        price=[]
        try:
            _thread.start_new_thread(s.name1,(s1,name))
            _thread.start_new_thread(s.price1,(s1,price))
        except:
            pass
        print(name)
        print(price)
        
        for i in s1.findAll('span',{'class':'style__pro-title___3zxNC'}):
            name.append(i.text)
        for i in s1.findAll('div',{'class':'style__price-tag___B2csA'}):
            price.append(i.text)
       
        '''
        for i in list1:
            str="https://www.1mg.com"+i
            data=r.request('get',str)
            print(data.ok)
            s1=bs4.BeautifulSoup(data.text,'html.parser')
            name.append((s1.find('h1',{'class':'ProductTitle__product-title___3QMYH'})).text)
            price.append((s1.find('div',{'class':'PriceDetails__discount-div___nb724'})).text)
            
        for i in list2:
            str="https://www.1mg.com"+i
            data=r.request('get',str)
            print(data.ok)
            s2=bs4.BeautifulSoup(data.text,'html.parser')
            try:
                price.append((s2.find('div',{'class':'DrugPriceBox__best-price___32JXw'})).text)
                name.append((s2.find('h1',{'class':'DrugHeader__title___1NKLq'})).text)
            except:
                pass
        list1.append(list2)'''
        for i in range(len(name)):
            print(name[i],price[i])
            
        s.display(len(name),name,price)
        
    def scrap(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('900x600+200+50')#'widthxheight+x+y
        s.scr.config(bg='khaki1')
        l=Label(s.scr,bg='blue',font=('times',30,'bold'),text='Enter your query to search')
        l.pack(side=TOP,fill=X)
        query=Entry(s.scr,bg='white',fg='black',font=('times',30,'bold'))
        query.place(x=250,y=100)
        searc=Button(s.scr,command=lambda :s.search(query.get()),text='SEARCH',bg='blue',fg='white',font=('times',30,'bold'))
        searc.place(x=350,y=200)
        s.scr.mainloop()
        
    def register(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1200x600+0+0')#'widthxheight+x+y
        s.scr.config(bg='khaki1')
        l=Label(s.scr,bg='blue',font=('times',30,'bold'),text='Welcome to Sqlite browser')
        l.pack(side=TOP,fill=X)
        l1=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Username')
        l1.place(x=300,y=100)
        l2=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Password')
        l2.place(x=300,y=200)
        l3=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Re password')
        l3.place(x=300,y=300)
        l4=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Email')
        l4.place(x=300,y=400)
        user=Entry(s.scr,bg='blue',fg='white',font=('times',30,'bold'))
        user.place(x=600,y=100)
        ps=Entry(s.scr,show='*',bg='blue',fg='white',font=('times',30,'bold'))
        ps.place(x=600,y=200)
        ps1=Entry(s.scr,show='*',bg='blue',fg='white',font=('times',30,'bold'))
        ps1.place(x=600,y=300)
        email=Entry(s.scr,bg='blue',fg='white',font=('times',30,'bold'))
        email.place(x=600,y=400)
        b=Button(s.scr,command=lambda :s.regi(user.get(),ps.get(),ps1.get(),email.get()),text='register',bg='blue',fg='white',font=('times',30,'bold'))
        b.place(x=600,y=500)
        b1=Button(s.scr,command=s.loginpage,text='back',bg='blue',fg='white',font=('times',30,'bold'))
        b1.place(x=300,y=500)
        s.scr.mainloop()
    def regi(s,u,p,p1,e):
        if not(re.search(r'^\S+$',u)):
               messagebox.showerror('register','user name must not contain spaces')
        if not(re.search(r'^\S+$',p)):
               messagebox.showerror('register','password must not contain spaces')
        if not(re.search(r'^\S+$',e)):
               messagebox.showerror('register','email must not contain spaces')

        s.scrap()
        
            
    def fun(s,a,b):
        
        if re.search(r'^\S+$',a) and re.search(r'^\S+$',b):
            clientsql=sql.connect(r'D:\GALLANT DECOY\Documents\#Python\miniproject\user.db')
            cu=clientsql.cursor()
            cu.execute('select * from student where name="$a" and fee="$b"')
            ls=list(*cu.fetchall())
            try:
                if a==ls[1] and b==ls[2]:
                    print("successfull")                              
            except:
                messagebox.showerror('login','invalid username or password')
        else:
            messagebox.showerror('login','user name must not contain spaces')
    def loginpage(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1200x600+0+0')#'widthxheight+x+y
        s.scr.config(bg='khaki1')
        l=Label(s.scr,bg='blue',font=('times',30,'bold'),text='Medicine finder')
        l.pack(side=TOP,fill=X)
        l1=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Username')
        l1.place(x=300,y=200)
        l2=Label(s.scr,bg='blue',fg='white',font=('times',30,'bold'),text='Password')
        l2.place(x=300,y=300)
        user=Entry(s.scr,bg='blue',fg='white',font=('times',30,'bold'))
        user.place(x=600,y=200)
        ps=Entry(s.scr,show='*',bg='blue',fg='white',font=('times',30,'bold'))
        ps.place(x=600,y=300)
        b=Button(s.scr,text='Login',command=lambda :s.fun(user.get(),ps.get()),bg='blue',fg='white',font=('times',30,'bold'))
        b.place(x=300,y=400)
        b1=Button(s.scr,command=s.register,text='New user',bg='blue',fg='white',font=('times',30,'bold'))
        b1.place(x=600,y=400)
        message=Label(s.scr,font=('times',15,'italic'),text='')
        message.place(x=700,y=500)
        s.scr.mainloop()
Gui()
