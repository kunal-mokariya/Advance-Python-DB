from tkinter import*;
from tkinter import ttk;
import csv
root = Tk();
root.title("SC");

tree = ttk.Treeview(root,columns=("id","name","price"),show="headings");
tree.heading("id",text="id")
tree.heading("name",text="name")
tree.heading("price",text="price")
tree.column(0,width=40,anchor="center")
tree.column(1,width=60,anchor="center")
tree.column(2,width=60,anchor="center")
tree.pack(padx=10,pady=20,fill="both",expand=False);
with open("my.txt","r",newline="") as f:
    row = csv.reader(f);
    for i in row:
        tree.insert("",END,values=(i))

root.geometry("600x600");
root.mainloop();