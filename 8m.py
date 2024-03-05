import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

password = " "
question = " "
name = " "
# Создание последнего окна
def new_window():
    window = tk.Tk()
    window.title("Приглашение")
    window.attributes("-topmost", True)
        
    info = tk.Label(window, text= "Приглашаем Вас сюда для открытия \n этого замечательного праздника \n на 1 этаж в 12:00!!", font=("Verdana",20), fg="PaleVioletRed3")
    info.pack()
        
    image = Image.open('//10.50.100.25/isc/Для ОБМЕНА/test_copy/3s.jpg')
    photo_sec = ImageTk.PhotoImage(image)
    label_1 = tk.Label(window, image=photo_sec)
    label_1.image = photo_sec
    label_1.pack()
        
    but = tk.Button(window, text="Закрыть окно", command=lambda: window.destroy(), bg="PaleVioletRed3", fg="black")
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
    
    #Создаем приветствие
    info_1 = tk.Label(root, text="С 8 марта, {}".format(name), font=("Verdana",20), fg="PaleVioletRed3", anchor="n")
    info_1.pack()    
    
    # Загружаем изображение
    image = Image.open('//10.50.100.25/isc/Для ОБМЕНА/test_copy/2s.jpg')
    photo = ImageTk.PhotoImage(image)

    # Создаем виджет для отображения изображения
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
        
    # Создаем вопрос
    info = tk.Label(root, text="Отгадайте загадку и введите ответ.\n {}".format(question), font=("Verdana",20), fg="PaleVioletRed3")
    info.pack()
        
    # Создаем поле для ввода кода
    entry = tk.Entry(root)
    entry.pack()
    
    # Функция для проверки введенного кода
    def check_code():
        passw = entry.get()
        passw = passw.strip()
        passw = passw.lower()
        if passw == password:
            root.destroy()
            new_window()
        else:
            messagebox.showinfo("Неверный код", "А вот и нет, нужно ввести код еще раз")

    # Создаем кнопку для ввода кода
    button = tk.Button(root, text="Ввести ответ", command=check_code, bg="PaleVioletRed3", fg="black")
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

info = tk.Label(main, text= "Введите вашу фамилию", font=("Verdana",20), fg="PaleVioletRed3")
info.pack()
        
# Создаем поле для ввода кода
entry = tk.Entry(main)
entry.pack()

# Функция проверки фамилии
def check_surname():
    global question
    global password
    global name
    surname = entry.get()
    surname = surname.strip()
    surname = surname.lower()
    if surname == "павлович":
        password = "календарь"
        question = "На раскрашенных страницах много праздников хранится"
        name = "Анна Павловна"
        main.destroy()
        sec_window()
    elif surname == "литвиненко":
        password = "подснежник"
        question = "Белый, синий, голубой. \n Появился он весной."
        name = "Анастасия Александровна"
        main.destroy()
        sec_window()
    elif surname == "ларьков":
        password = "спасибо"
        question = "Волшебное слово?"
        name = "Жулик"
        main.destroy()
        sec_window()
    elif surname == "малинская":
        password = "порядка"
        question = "Чего нет в женской сумочке?"
        name = "Анастасия Николаевна"
        main.destroy()
        sec_window()
    elif surname == "шутова":
        password = "конфеты"
        question = "Что мужчины всей планеты \n Дарят женщинам?..."
        name = "Галина Григорьевна"
        main.destroy()
        sec_window()
    elif surname == "александрович":
        password = "февраль"
        question = "В каком месяце болтушка Валя говорит меньше всего?"
        name = "Анна Викторовна"
        main.destroy()
        sec_window()
    elif surname == "юзефович":
        password = "подснежник"
        question = "Белый, синий, голубой. \n Появился он весной."
        name = "Елена Валерьевна"
        main.destroy()
        sec_window()
    elif surname == "кочубей":
        password = "конфеты"
        question = "Что мужчины всей планеты \n Дарят женщинам?..."
        name = "Ксения Владимировна"
        main.destroy()
        sec_window()
    elif surname == "заяц":
        password = "порядка"
        question = "Чего нет в женской сумочке?"
        name = "Татьяна Владимировна"
        main.destroy()
        sec_window()
    elif surname == "дмитренок":
        password = "февраль"
        question = "В каком месяце болтушка Валя говорит меньше всего?"
        name = "Валентина Ивановна"
        main.destroy()
        sec_window()
    elif surname == "веремейчик":
        password = "календарь"
        question = "На раскрашенных страницах много праздников хранится"
        name = "Ольга Геннадьевна"
        main.destroy()
        sec_window()
    else:
        messagebox.showinfo("Неправильная фамилия", "Проверьте правильность фамилии! Попробуйте ещё раз!!!")

# Создаем кнопку для ввода кода
button = tk.Button(main, text="Ввести фамилию", command=check_surname, bg="PaleVioletRed3", fg="black")
button.pack()
     
# Запускаем главный цикл обработки событий
main.mainloop()

