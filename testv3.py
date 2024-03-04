import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

buf = 0
password = "Спасибо"

def not_closing():
    if messagebox.askokcancel("А ВОТ И НЕТ!!!", "А ВОТ И НЕ ПОЛУЧИТСЯ!!!!"):
        pass

while True:
    
    # Создаем главное окно
    root = tk.Tk()
    root.title("С 8 Марта")
    root.attributes("-topmost", True)
    root.attributes("-toolwindow", True)
    root.protocol("WM_DELETE_WINDOW", not_closing)
    
    # Загружаем изображение
    photo = ImageTk.PhotoImage(file= '//10.50.100.25/isc/Для ОБМЕНА/test_copy/8m.jpg')

    # Создаем виджет для отображения изображения
    label = tk.Label(root, image=photo)
    label.pack()
    

    # Функция для проверки введенного кода
    def check_code():
        if entry.get() == password:
            root.destroy()
            new_window()
            global buf
            buf = 1
        else:
            messagebox.showinfo("Неверный код", "А вот и нет, нужно ввести код еще раз")

    # Создание нового окна
    def new_window():
        window = tk.Tk()
        window.title("Приглашение")
        window.attributes("-topmost", True)
        
        info = tk.Label(window, text= "Приглашаем Вас на банкет сюда", font=("Verdana",20), fg="red")
        info.pack()
        
        image = Image.open('//10.50.100.25/isc/Для ОБМЕНА/test_copy/hall.jpg')
        photo_sec = ImageTk.PhotoImage(image)
        label_1 = tk.Label(window, image=photo_sec)
        label_1.image = photo_sec
        label_1.pack()
        
        but = tk.Button(window, text="Закрыть окно", command=lambda: window.destroy(), bg="red", fg="black")
        but.pack()
    
    # Создаем поле для ввода кода
    entry = tk.Entry(root)
    entry.pack()
    
    # Создаем кнопку для ввода кода
    button = tk.Button(root, text="Ввести код", command=check_code, bg="red", fg="black")
    button.pack()
    
    
    if buf == 1:
       break
    
    # Запускаем главный цикл обработки событий
    root.mainloop()

