from model import Timer
from pizco import Server
import tkinter as tk

#
root = tk.Tk()
server = Server(Timer(root), 'tcp://127.0.0.1:8000')
root.mainloop()
server.serve_forever()

