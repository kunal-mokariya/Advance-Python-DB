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
with open("my.txt","w",newline="") as f:
    row = csv.writer(f);
    row.writerow(["id","name","city"])
    rows = ([["1","kunal","ksd"],["2","rohit","jnd"],["3","meet","rjk"]]);
    row.writerows(rows)
    for i in rows:
        tree.insert("",END,values=(i))

root.geometry("600x600");
root.mainloop();