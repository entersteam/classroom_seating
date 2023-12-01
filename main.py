import pandas as pd
import numpy as np
import tkinter as tk

file_path = 'students.csv'

data = pd.read_csv(file_path)

row, col, group = 5, 2, 3
group_line_col = [i*(1+col)-1 for i in range(1,group)]

root = tk.Tk()
root.title('seogo_class_tool')

root.geometry("1000x650")

root.resizable(width=False, height=False)


classroom_frame = tk.Frame(root)
white_board = tk.Button(root, text='칠판',bg='white',font = ('Arial', 20),width=20, height=3)
white_board.pack(side=tk.TOP, padx=5, pady=10)
classroom_frame.pack(side=tk.BOTTOM, padx=50, pady=10)

for i in range(row):
    row_frame = tk.Frame(classroom_frame)
    row_frame.pack(side=tk.TOP)
    
    for j in range((col + 1) * group - 1):
        btn = tk.Button(row_frame, width=10,bg='green', height=5,padx=20)
        if j in group_line_col:
            btn.config(bg='white')
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        
root.mainloop()