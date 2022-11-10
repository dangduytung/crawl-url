
import tkinter as tk
import threading
from datetime import datetime

import CrawlUrl


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.insert = tk.Entry(self)
        self.insert.pack(side="top", ipadx=200, padx=20, pady=20)
        self.insert.focus_set()

        self.btn_submit = tk.Button(self)
        self.btn_submit["text"] = "Click Here"
        self.btn_submit["command"] = self.execute_crawl_url
        self.btn_submit.pack(side="top")

        self.quit = tk.Button(
            self, text="QUIT", fg="red", command=root.destroy
        )

        self.quit.pack(side="bottom")

    def execute_crawl_url(self):
        url = self.insert.get()
        print(str(datetime.now()) + " ~ Start crawl url: " + url)
        obj_crawl_url = CrawlUrl.CrawlUrl(url)
        process = threading.Thread(
            target=obj_crawl_url.main(), name="t1", daemon=True
        )
        process.start()


root = tk.Tk()
root.wm_title("Crawl links of site")
app = Application(master=root)
app.mainloop()
