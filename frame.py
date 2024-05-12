import tkinter as tk
import threading
import time
import pyautogui

class AutoClicker:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Auto Clicker")
        self.width = 150
        self.height = 150
        self.clicks = 0
        self.click_speed = 0
        self.clicking = False
        self.click_thread = None
        self.counter_label = None
        self.root.bind("<Control-s>", self.start_clicking)
        self.root.bind("<Control-p>", self.stop_clicking)
        self.root.bind("<Control-q>", self.close_window)

    def set_size(self, width: int, height: int):
        self.width = width
        self.height = height
        self.root.geometry(f"{self.width}x{self.height}")

    def set_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")

    def close_button(self):
        self.close_button = tk.Button(self.root, text="Close (Ctrl+q)", command=self.root.destroy)
        self.close_button.pack(side="bottom", pady=10, padx=10)

    def start_button(self):
        self.start_button = tk.Button(self.root, text="Start (Ctrl+s)", command=self.start_clicking)
        self.start_button.pack(side="bottom", pady=10, padx=10)

    def stop_button(self):
        self.stop_button = tk.Button(self.root, text="Stop (Ctrl+p)", command=self.stop_clicking)
        self.stop_button.pack(side="bottom", pady=10, padx=10)

    def click_speed_entry(self):
        self.click_speed_label = tk.Label(self.root, text="Click Speed (ms):")
        self.click_speed_label.pack(side="bottom", pady=5, padx=10)
        self.click_speed_var = tk.StringVar()
        self.click_speed_entry = tk.Entry(self.root, textvariable=self.click_speed_var)
        self.click_speed_entry.pack(side="bottom", pady=5, padx=10)

    def number_of_clicks_label(self):
        self.counter_label = tk.Label(self.root, text="0", font=("Arial", 24), bg="lightblue", width=6, height=2)
        self.counter_label.place(relx=0.5, rely=0.5, anchor="center")

    def start_clicking(self, event=None):
        if not self.clicking:
            self.click_speed = int(self.click_speed_var.get())
            self.clicking = True
            self.click_thread = threading.Thread(target=self.click_thread_function)
            self.click_thread.start()

    def stop_clicking(self, event=None):
        self.clicking = False
    def click_thread_function(self):
        while self.clicking:
            pyautogui.click()
            self.clicks += 1
            self.root.after(100, self.update_counter)
            time.sleep(self.click_speed / 1000)

    def update_counter(self):
        self.counter_label.config(text=str(self.clicks))
    def close_window(self, event=None):
        self.root.destroy()
    def run(self):
        self.set_size(self.width, self.height)
        self.set_frame()
        self.close_button()
        self.start_button()
        self.stop_button()
        self.click_speed_entry()
        self.number_of_clicks_label()
        self.root.mainloop()

if __name__ == "__main__":
    clicks = AutoClicker()
    clicks.run()
