import os
import tkinter as tk
import pygame

def callback(selection):
    print(f"Selected \"{selection}\"")
    return

if __name__ == '__main__':
    # print(os.environ.get('DISPLAY', ''))
    top = tk.Tk() #creating tkinter window

    sort_frame = tk.Frame(top)
    sort_frame.pack()

    sort_label = tk.Label(sort_frame, text = "Sorting Algorithm: ")
    sort_label.pack( side = tk.LEFT )

    sorting_algorithms = ["A*", "Djikstra\'s", "Bellman Ford", "Floyd-Warshall\'s"]
    option = tk.StringVar(top)
    option.set("A*") #set default option
    callback(option.get())
    #note you can get the current output with option.get()

    sort_opt = tk.OptionMenu(sort_frame, option, *sorting_algorithms, command=callback)
    sort_opt.pack( side = tk.LEFT )

    top.mainloop() #run tkinter window
