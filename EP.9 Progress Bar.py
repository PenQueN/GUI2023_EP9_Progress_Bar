import threading
import time
import tkinter as tk
from tkinter import ttk

GUI = tk.Tk()

GUI.overrideredirect(True)
GUI.geometry('500x150+500+300')
GUI.resizable(False, False)
GUI.config(bg='#222')
label = ttk.Label(GUI, text='Loading...', font=('Arial', 20), foreground='#fff', background='#222')
label.pack(pady=20)
progressbar = ttk.Progressbar(GUI, orient='horizontal', length=400, mode='determinate')
progressbar.pack(pady=20)

def progress():
    for i in range(100):
        progressbar['value'] = i+1
        time.sleep(0.03)
    GUI.destroy()


progress_thread = threading.Thread(target=progress)
progress_thread.start()

GUI.mainloop()

GUI2 = tk.Tk()
GUI2.geometry('500x100+500+300')
GUI2.config(bg='#222')

label2 = ttk.Label(GUI2,text='Hello World', font=('Arial', 20), foreground='#fff', background='#222')
label2.pack(pady=20)

GUI2.mainloop()