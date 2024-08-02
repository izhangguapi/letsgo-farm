import tkinter as tk

def delete_top_item():
    if len(listbox.get(0, tk.END)) > 100:
        listbox.delete(0, 0)

root = tk.Tk()

listbox = tk.Listbox(root, height=100, width=60)
listbox.pack()

for i in range(150):
    listbox.insert(tk.END, f"Item {i}")

    if len(listbox.get(0, tk.END)) > 100:
        listbox.delete(0, 0)

root.mainloop()
