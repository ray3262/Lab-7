import tkinter as tk
from tkinter import PhotoImage
import requests
from io import BytesIO
from PIL import Image, ImageTk


def get_random_fox_image():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)  
    data = response.json()  
    image_url = data['image']  
    return image_url


def update_image():
    image_url = get_random_fox_image()  
    response = requests.get(image_url)  
    img_data = response.content  
    img = Image.open(BytesIO(img_data))  
    img = img.resize((400, 400), Image.Resampling.LANCZOS)  
    img_tk = ImageTk.PhotoImage(img)  

    
    label.config(image=img_tk)
    label.image = img_tk  


root = tk.Tk()
root.title("Générateur d'images de renards")


label = tk.Label(root)
label.pack(padx=10, pady=10)


button = tk.Button(root, text="следующее изображение", command=update_image)
button.pack(pady=10)


update_image()


root.mainloop()
