import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Создаем главное окно
root = tk.Tk()
root.title("С 8 Марта")

# Загружаем изображение
photo = ImageTk.PhotoImage(file= '//10.50.100.25/isc/10_ЦЗИТ/ER/mart.jpg')

# Создаем виджет для отображения изображения
label = tk.Label(root, image=photo)
label.pack()

# Функция для проверки введенного кода
def check_code():
    if entry.get() == "спасибо":
        root.destroy()
    else:
        messagebox.showinfo("Неверный код", "Попробуйте ввести код еще раз")

# Создаем поле для ввода кода
entry = tk.Entry(root, show="*")
entry.pack()

# Создаем кнопку для ввода кода
button = tk.Button(root, text="Ввести код", command=check_code)
button.pack()

# Запускаем главный цикл обработки событий
root.mainloop()