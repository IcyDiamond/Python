import tkinter as tk
from instaloader import *
from PIL import ImageTk,Image
import os
import threading


class Download(tk.Tk):
    def __init__(self):
        super().__init__()
        self.insta = instaloader.Instaloader()
        self.title("Insta Downloader")
        self.geometry("200x150")
        self.input_field = tk.Entry(self)
        self.input_field.pack()
        confirm = tk.Button(self, text="Download" , command = self.download_post)
        confirm.pack()
        self.image_display = tk.Label(self)
        self.image_display.pack()

    def download_post(self):
        self.insta_post_code = self.input_field.get()
        self.insta_post_code = self.insta_post_code.split('/')
        self.insta_post_code = self.insta_post_code[len(self.insta_post_code)-2:-1]
        self.insta_post_code = self.insta_post_code[0]
        post = Post.from_shortcode(self.insta.context, self.insta_post_code)
        self.insta.download_post(post, target=f"temp-{self.insta_post_code}")
        self.get_image()
    
    def get_image(self):
        self.folder_items = os.listdir(f"temp-{self.insta_post_code}")
        for fichier in self.folder_items[:]: # filelist[:] makes a copy of filelist.
            if not(fichier.endswith(".jpg")):
                self.folder_items.remove(fichier)
        self.x = threading.Thread(target=self.update_img, daemon=True).start()

    def update_img(self):
        self.insta_post = ImageTk.PhotoImage(Image.open(f"temp-{self.insta_post_code}\\{self.folder_items[0]}").resize((self.winfo_width(),self.winfo_height())))
        self.image_display.configure(image=self.insta_post)
        



if __name__ == "__main__":
    app = Download()
    app.mainloop()