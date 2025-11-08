import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns=("col1", "col2"), show='tree headings')
tree.heading("#0", text="Category")
tree.heading("col1", text="Value1")
tree.heading("col2", text="Value2")

tree.column("#0", width=150)
tree.column("col1", width=100)
tree.column("col2", width=100)

# Parent
p1 = tree.insert("", "end", text="Parent A", values=("A1","A2"))

# Child of Parent A
tree.insert(p1, "end", text="Child A1", values=("A1-1","A1-2"))
tree.insert(p1, "end", text="Child A2", values=("A2-1","A2-2"))

# Another parent
p2 = tree.insert("", "end", text="Parent B", values=("B1","B2"))
tree.insert(p2, "end", text="Child B1", values=("B1-1","B1-2"))

tree.pack(expand=True, fill='both')
root.mainloop()
