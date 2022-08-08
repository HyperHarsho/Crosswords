import tkinter as tk
import main as table
table.main()
m = tk.Tk()
for i in range(len(table.TABLE)):
    for j in range(len(table.TABLE[i])):
        frame = tk.Frame(
            master=m,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(
            master=frame, text=table.TABLE[i][j], width=7, height=3)
        label.pack()
m.mainloop()
