import tkinter as tk
import threading

class App:
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(master, text='Load Data', command=self.load_data)
        self.button.pack()
        self.progress = tk.Label(master, text='Ready')
        self.progress.pack()

    def load_data(self):
        self.progress['text'] = 'Loading...'
        thread = threading.Thread(target=self._load_data, args=(self.on_data_loaded,))
        thread.start()

    def on_data_loaded(self, data):
        self.progress['text'] = 'Data loaded'
        # update GUI with loaded data

    def _load_data(self, callback):
        # load data from network or file
        data = load_data()
        callback(data)

def load_data():
    # load data from network or file
    return []

root = tk.Tk()
app = App(root)
root.mainloop()