import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
from datetime import datetime, timedelta

API_KEY = "qIvOMBTdIUgNAuSbycWa38xT6iGuNE62inHfNKC3"
BASE_URL = "https://api.nasa.gov/planetary/apod"

def get_latest_image():
    """Получает URL изображения за последние 5 дней, игнорируя видео."""
    for i in range(5):  
        date = (datetime.today() - timedelta(days=i)).strftime("%Y-%m-%d")
        params = {"api_key": API_KEY, "date": date}
        
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get("media_type") == "image":  
                return data['url'], data['explanation']
    
    return None, "Нет доступных изображений за последние 5 дней."

def update_image():
    image_url, explanation = get_latest_image()
    
    if image_url:
        try:
            img_response = requests.get(image_url)
            img_response.raise_for_status()
            
            img_data = img_response.content
            img = Image.open(BytesIO(img_data))  
            img = img.resize((600, 400), Image.Resampling.LANCZOS)  
            img_tk = ImageTk.PhotoImage(img)  
            
            label.config(image=img_tk)
            label.image = img_tk  
            
            explanation_label.config(text=explanation)
        except Exception as e:
            print(f"Ошибка при загрузке изображения: {e}")
    else:
        explanation_label.config(text=explanation)

root = tk.Tk()
root.title("Фото дня от NASA")

label = tk.Label(root)
label.pack(padx=10, pady=10)

explanation_label = tk.Label(root, text="", wraplength=500)
explanation_label.pack(pady=10)

button = tk.Button(root, text="Получить новое фото", command=update_image)
button.pack(pady=10)

update_image()

root.mainloop()
