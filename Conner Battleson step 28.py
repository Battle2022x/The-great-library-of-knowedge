#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.title("vommit.py")
root.wm_geometry("400x400")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)
frame4 = tk.Frame(root)


frame1.grid(row = "0", column = "0")
blue = tk.Label(frame1, bg = "blue", width = "33", height = "15")
blue.pack()


frame2.grid(row = "1", column = "0")
red = tk.Label(frame2, bg = "red", width = "33", height = "15")
red.pack()

frame3.grid(row = "1", column = "1")
yellow = tk.Label(frame3, bg = "yellow", width = "33", height = "15")
yellow.pack()

frame4.grid(row = "0", column = "1")
green = tk.Label(frame4, bg = "#AAFF00", width = "33", height = "15")
green.pack()

root.mainloop()