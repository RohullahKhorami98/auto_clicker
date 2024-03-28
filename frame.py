import tkinter as tk



root = tk.Tk()
root.geometry()
main_frame = tk.Frame(root)

close_button = tk.Button(root,text="Close",command=root.destroy)
close_button.place(x=20,y=20)
main_frame.pack()


root.mainloop()