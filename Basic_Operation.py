import tkinter as tk;
import _sqlite3 as sq;

root = tk.Tk();
root.title("MY");
name = tk.StringVar();
city = tk.StringVar();
age = tk.IntVar();
#Data Insert
def insert_data():
    cnn = sq.connect("my.db");
    cursor = cnn.cursor();
    cursor.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,city TEXT,age INTEGER)")
    cursor.execute("insert into test(name,city,age)values(?,?,?)",(name.get(),city.get(),age.get()))
    cursor.close();
    cnn.commit();
    cnn.close();

lbl1 = tk.Label(root,text="Name");
lbl1.place(x=20,y=30)
txt1 = tk.Entry(root,textvariable=name);
txt1.place(x=80,y=30)

lbl2 = tk.Label(root,text="city");
lbl2.place(x=20,y=60);
txt2 = tk.Entry(root,textvariable=city);
txt2.place(x=80,y=60)


lbl3= tk.Label(root,text="Age");
lbl3.place(x=20,y=90);
txt3 = tk.Entry(root,textvariable=age,text="");
txt3.place(x=80,y=90)

btn1 = tk.Button(root,text="Insert Data",command=insert_data);
btn1.place(x=80,y=300)

root.geometry("500x500")
root.mainloop();
