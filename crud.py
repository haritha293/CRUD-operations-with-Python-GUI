from tkinter import *
import tkinter.messagebox as MessageBox
import MySQLdb as mysql
def Insert():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
    sql="Insert into person values(%s,%s,%s)"
    vals=(id,name,phone)
    if(id == "" or name == "" or phone == ""):
       MessageBox.showinfo("ALERT", "Please enter all fields")
    else:
       con = mysql.connect(host="localhost", user="root", password="Root", database="mydbs")
       cursor = con.cursor()
       cursor.execute(sql,vals)
       cursor.execute("commit")
       MessageBox.showinfo("Status", "Successfully Inserted")
       con.close()
       
       id_entry.delete(0, END)
       name_entry.delete(0, END)
       phone_entry.delete(0, END)
    
def Delete():
    if(id_entry.get() == ""):
       MessageBox.showinfo("ALERT", "Please enter ID to delete row")
    else:
       sql="Delete from person where id=%s"
       con = mysql.connect(host="localhost", user="root", password="Root", database="mydbs")
       cursor = con.cursor()
       vals=(id_entry.get(),)
       cursor.execute(sql,vals)
       con.commit()
       cnt=cursor.rowcount
       if cnt>=1:
          MessageBox.showinfo("Status", "Successfully Deleted")
       else:
           MessageBox.showinfo("Status", "Delete Failed")
            
       con.close()
def Update():
    id = id_entry.get()
    name = name_entry.get()
    phone = phone_entry.get()
  
    if(name == "" or phone == ""):
       MessageBox.showinfo("ALERT", "Please enter fiels you want to update!")
    else:
        sql="Update person set name=%s, phone=%s where id=%s"
        vals=(name,phone,id)
        con = mysql.connect(host="localhost", user="root", password="Root", database="mydbs")
        cursor = con.cursor()
        cursor.execute(sql,vals)
        con.commit()
        cnt=cursor.rowcount
        if cnt>=1:
         MessageBox.showinfo("Status", "Successfully Updated")
        else:
         MessageBox.showinfo("Status", "Update Failed")
        con.close()
    
def Select():
    if(id_entry.get() == ""):
       MessageBox.showinfo("ALERT","ID is required to select row!")
    else:
       sql="select * from person where id=%s"
       id=id_entry.get()
       vals=(id,)
       con = mysql.connect(host="localhost", user="root", password="Root", database="mydbs")
       cursor = con.cursor()
       cursor.execute(sql,vals)
       rows = cursor.fetchall()
  
    for row in rows:
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        name_entry.insert(0, row[1])
        phone_entry.insert(0, row[2])
    con.close()

root=Tk()
root.geometry("500x300")
root.title("Mysql CRUD Operations")
id=Label(root,text="Enter ID:", font=("verdana 15"))
id.place(x=50,y=30)
id_entry=Entry(root,font=("verdana 15"))
id_entry.place(x=150,y=30)
name=Label(root,text="Name:", font=("verdana 15"))
name.place(x=50,y=80)
name_entry=Entry(root,font=("verdana 15"))
name_entry.place(x=150,y=80)
phone=Label(root,text="Phone:", font=("verdana 15"))
phone.place(x=50,y=130)
phone_entry=Entry(root,font=("verdana 15"))
phone_entry.place(x=150,y=130)
btnInsert=Button(root,text="Insert",command=Insert, font=("verdana 15")).place(x=100,y=190)
btnDelete=Button(root,text="Delete",command=Delete, font=("verdana 15")).place(x=200,y=190)
btnUpdate=Button(root,text="Update",command=Update, font=("verdana 15")).place(x=320,y=190)
btnSelect=Button(root,text="Select",command=Select, font=("verdana 15")).place(x=200,y=240)
root.mainloop()