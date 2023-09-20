import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("文本编辑器")
        self.filename = None

        # 创建菜单栏
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # 创建文件菜单
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="新建", command=self.new_file)
        file_menu.add_command(label="打开", command=self.open_file)
        file_menu.add_command(label="保存", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.master.quit)

        # 创建编辑菜单
        edit_menu = tk.Menu(menu)
        menu.add_cascade(label="编辑", menu=edit_menu)
        edit_menu.add_command(label="复制", command=self.copy)
        edit_menu.add_command(label="粘贴", command=self.paste)

        # 创建工具栏
        tool_bar = tk.Frame(self.master, bd=1, relief=tk.RAISED)
        tool_bar.pack(side=tk.TOP, fill=tk.X)

        # 创建按钮
        new_button = tk.Button(tool_bar, text="新建", command=self.new_file)
        new_button.pack(side=tk.LEFT, padx=2, pady=2)
        open_button = tk.Button(tool_bar, text="打开", command=self.open_file)
        open_button.pack(side=tk.LEFT, padx=2, pady=2)
        save_button = tk.Button(tool_bar, text="保存", command=self.save_file)
        save_button.pack(side=tk.LEFT, padx=2, pady=2)

        # 创建文本框
        self.text = tk.Text(self.master, wrap=tk.WORD)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.filename = None

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            self.text.delete("1.0", tk.END)
            with open(self.filename, "r") as f:
                self.text.insert(tk.END, f.read())

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get("1.0", tk.END))

    def copy(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    def paste(self):
        self.text.insert(tk.INSERT, self.text.clipboard_get())

if __name__ == '__main__':
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()