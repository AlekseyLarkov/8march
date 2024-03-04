import tkinter as tk
from PIL import Image, ImageTk

class ImageWindow:
    def __init__(self, master, image_path, password):
        self.master = master
        self.image_path = image_path
        self.password = password
        
        self.canvas = tk.Canvas(self.master, width=508, height=718)
        self.canvas.pack()
        
        self.img = Image.open(self.image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        
        self.master.bind("<Key>", self.check_password)
        
    def check_password(self, event):
        if event.char == self.password:
            self.master.destroy()

image_path = "mart.jpg"
password = "p"

root = tk.Tk()
root.title("С 8 Марта")
root.attributes("-topmost", True)

app = ImageWindow(root, image_path, password)

root.mainloop()