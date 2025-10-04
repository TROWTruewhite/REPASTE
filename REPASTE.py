import tkinter as tk
import tkinter.ttk as ttk
import pynput.keyboard as k
from time import sleep

c = k.Controller()

def paste(text, listbox, root):
    for i in range(5):
        listbox.insert(tk.END, f'将在{5-i}秒后粘贴，请尽快将焦点放到要粘贴的位置')
        listbox.see(tk.END)
        root.update()
        sleep(1)
    c.type(text)
    listbox.insert(tk.END, f'已粘贴：{text}')
    listbox.see(tk.END)

def window():
    root = tk.Tk()
    root.title("REPASTE")
    root.resizable(False, False)
    
    ttk.Label(root, text="请输入要粘贴的内容：").pack(pady=10)
    text_frame = tk.Frame(root)
    text_frame.pack()
    init_data_Text = tk.Text(text_frame, width=100, height=20)
    init_data_Text.grid(row=0, column=0)
    ttk.Button(root, text="粘贴", width=10, command=lambda: paste(init_data_Text.get('1.0', tk.END).rstrip('\n'), log_listbox, root)).pack(pady=10)
    list_frame = ttk.LabelFrame(root, text='日志')
    list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

    scrollbar = ttk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    log_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, selectmode=tk.EXTENDED)
    log_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    scrollbar.config(command=log_listbox.yview)

    ttk.Label(root, text="Made by True_white_").pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    window()
