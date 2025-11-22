from tkinter import*;
from tkinter import ttk;
import mysql.connector as sq;
import csv
root = Tk();
root.title("SC");

def init():
    cnn = sq.connect(host="localhost",user="root",password="",database="somnath");
    cursor = cnn.cursor();
    cursor.execute("create table if not exists My(id int primary key auto_increment,name varchar(20),city varchar(30))")
    cursor.close();
    cnn.close();
init();

def save_data():
    with open("my.txt","a",newline="") as f:
        cnn = sq.connect(host="localhost",user="root",password="",database="somnath");
        cursor = cnn.cursor();
        cursor.execute("insert into My(name,city)",(txt1.get(),txt2.get()));
        cnn.commit();
        cursor.close();
        cnn.close();
        row = csv.writer(f);
        row.writerow([cursor.lastrowid,txt1.get(),txt2.get()]);
        tree.insert("",END,values=(cursor.lastrowid,txt1.get(),txt2.get()))
        txt1.delete(0,END);
        txt2.delete(0,END);
    
txt1 = Entry(root);
txt1.pack(padx=10,pady=10);
txt2 = Entry(root);
txt2.pack(padx=10,pady=10);
btn1 = Button(root,text="Save",command=save_data);
btn1.pack(padx=10,pady=10);

tree = ttk.Treeview(root,columns=("id","name","price"),show="headings");
tree.heading("id",text="id")
tree.heading("name",text="name")
tree.heading("price",text="price")
tree.column(0,width=40,anchor="center")
tree.column(1,width=60,anchor="center")
tree.column(2,width=60,anchor="center")
tree.pack(padx=10,pady=20,fill="both",expand=False);


root.geometry("600x600");
root.mainloop();