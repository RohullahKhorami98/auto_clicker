import tkinter as tk


class autoClicker:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.width = 0
        self.height = 0
    def setSize(self,width:int, height:int):
        self.width = width
        self.height = height
        self.root.geometry(f"{self.width}x{self.height}")
    def setFrame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
    def closeButton(self):
        self.close_button = tk.Button(self.root,text="Close", command=self.root.destroy)
        self.close_button.place(x=20,y=20)
    def run(self):
        self.setSize(self.width,self.height)
        self.setFrame()
        self.closeButton()
        self.root.mainloop()



if __name__=="__main__":
    clicks = autoClicker()
    clicks.setSize(40,40)
    clicks.run()