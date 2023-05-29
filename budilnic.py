from tkinter import *  # Импорт библиотеки для создания объекта
import datetime
import time
import winsound
from threading import *
from winsound import PlaySound

root = Tk()  # Здесь создали объект
root.geometry("400x200")  # Задали размер окна


def Threading():  # threading - независимая последовательность выполнения вычислений
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    while True:
        # Устанавливаем время для будильника
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)  # Пауза в секунду для корректного отображения будильника и его звонка

        # Настройка для текущего времени
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Проверка соответствия установленного времени
        if current_time == set_alarm_time:
            print("Пора вставать, солнце!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


# Добавление метки, рамки, кнопки и меню опций
Label(root, text="Будильник", font=("Helvetica 22 bold"), fg="brown").pack(
    pady=10)  # 'Helvetica' - размер окна. 'Pady' - положение вертикально. 'Fg' - цвет текста
Label(root, text="Установите время", font=("Helvetica 11 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)  # Добавление настроек часов в меню
hrs.pack(side=LEFT)  # Настройка для положения справа налево

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)  # Добавление настроек минут в меню
mins.pack(side=LEFT)  # Настройка для положения справа налево

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)  # Добавление настроек секунд в меню
secs.pack(side=LEFT)  # Настройка для положения справа налево

Button(root, text="Сохранить", font=("Helvetica 11"), command=Threading).pack(
    pady=20)  # 'Helvetica' - размер окна. 'Pady' - положение вертикально.

# Выполнение заданного, нашим объектом
root.mainloop()