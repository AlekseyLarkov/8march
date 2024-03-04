import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

password = " "
question = " "

# Создание последнего окна
def new_window():
    window = tk.Tk()
    window.title("Приглашение")
    window.attributes("-topmost", True)
        
    info = tk.Label(window, text= "Приглашаем Вас сюда на банкет в 12:00!!", font=("Verdana",20), fg="red")
    info.pack()
        
    image = Image.open('//10.50.100.25/isc/Для ОБМЕНА/test_copy/3s.jpg')
    photo_sec = ImageTk.PhotoImage(image)
    label_1 = tk.Label(window, image=photo_sec)
    label_1.image = photo_sec
    label_1.pack()
        
    but = tk.Button(window, text="Закрыть окно", command=lambda: window.destroy(), bg="red", fg="black")
    but.pack()

#чтобы нельзя было закрыть окно
def not_closing():
    if messagebox.askokcancel("А ВОТ И НЕТ!!!", "А ВОТ И НЕ ПОЛУЧИТСЯ!!!!"):
        pass
 
# Создание второго окна
def sec_window():
       
    # Создаем главное окно
    root = tk.Tk()
    root.title("С 8 Марта")
    root.attributes("-topmost", True)
    root.attributes("-toolwindow", True)
    root.protocol("WM_DELETE_WINDOW", not_closing)
        
    # Загружаем изображение
    image = Image.open('//10.50.100.25/isc/Для ОБМЕНА/test_copy/2s.jpg')
    photo = ImageTk.PhotoImage(image)

    # Создаем виджет для отображения изображения
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
    
    # Создаем вопрос
    info = tk.Label(root, text= question, font=("Verdana",20), fg="red")
    info.pack()
        
    # Создаем поле для ввода кода
    entry = tk.Entry(root)
    entry.pack()
    
    # Функция для проверки введенного кода
    def check_code():
        if entry.get() == password:
            root.destroy()
            new_window()
        else:
            messagebox.showinfo("Неверный код", "А вот и нет, нужно ввести код еще раз")

    # Создаем кнопку для ввода кода
    button = tk.Button(root, text="Ввести код", command=check_code, bg="red", fg="black")
    button.pack()
  
# Создаем главное окно
main = tk.Tk()
main.title("С 8 Марта")
main.attributes("-topmost", True)
main.attributes("-toolwindow", True)
main.protocol("WM_DELETE_WINDOW", not_closing)

# Загружаем изображение
photo = ImageTk.PhotoImage(file= '//10.50.100.25/isc/Для ОБМЕНА/test_copy/1s.jpg')

# Создаем виджет для отображения изображения
label = tk.Label(main, image=photo)
label.pack()

info = tk.Label(main, text= "Введите вашу фамилию с большой буквы", font=("Verdana",20), fg="red")
info.pack()
        
# Создаем поле для ввода кода
entry = tk.Entry(main)
entry.pack()

# Функция проверки фамилии
def check_surname():
    global question
    global password
    surname = entry.get()
    surname = surname.strip()
    if surname == "Павлович":
        password = "1"
        question = "Первая цифра"
        main.destroy()
        sec_window()
    if surname == "Литвиненко":
        password = "2"
        question = "Вторая цифра"
        main.destroy()
        sec_window()
    if surname == "Ларьков":
        password = "Спасибо"
        question = "Волшебное слово?"
        main.destroy()
        sec_window()
    if surname == "Малинская":
        password = "3"
        question = "Третья?"
        main.destroy()
        sec_window()
    if surname == "Шутова":
        password = "4"
        question = "Четвертая?"
        main.destroy()
        sec_window()
    if surname == "Александрович":
        password = "5"
        question = "Пятая?"
        main.destroy()
        sec_window()
    if surname == "Юзефович":
        password = "6"
        question = "Шестая?"
        main.destroy()
        sec_window()
    if surname == "Кочубей":
        password = "7"
        question = "Седьмая?"
        main.destroy()
        sec_window()
    if surname == "Заяц":
        password = "8"
        question = "Восьмая?"
        main.destroy()
        sec_window()
    if surname == "Дмитренок":
        password = "9"
        question = "Девятая?"
        main.destroy()
        sec_window()
    if surname == "Веремейчик":
        password = "10"
        question = "Десятая?"
        main.destroy()
        sec_window()
    else:
        messagebox.showinfo("Неправильная фамилия", "Проверьте правильность фамилии! Попробуйте ещё раз!!!")

# Создаем кнопку для ввода кода
button = tk.Button(main, text="Ввести фамилию", command=check_surname, bg="red", fg="black")
button.pack()
     
# Запускаем главный цикл обработки событий
main.mainloop()

