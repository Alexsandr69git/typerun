from tkinter import *
from timeit import default_timer as timer
import random




def game():
    global x
    global x2

    if x == 0:
        # window.destroy()
        x = x + 1

    def check_result(event=None):

        input_text = entry.get()

        if input_text == words[word]:
            end = timer()
            x2.config(text="")
            print("ВЕРНО + ваше время =", end - start)
            print(entry.get())
            print(words[word])
            game()
        else:
            print("Ошибка ввода")
            print(entry.get())
            print(words[word])

    words = [
        'asterisk,звездочка',
        'background,фон',
        'backup,резкопия',
        'browsing,просмотр',
        'cancel,отменить',
        'checksum,контрсумма',
        'compatible,совместимый',
        'compute,вычислить',
        'connect,соединиться',
        'controller,диспетчер',
        'counter,счетчик',
        'data,данные',
        'debugger,отладчик',
        'default,умолчание',
        'desktop,рабочийстол',
        'device,устройство',
        'digest,дайджест',
        'digital,цифровой',
        'disable,отключить',
        'download,загрузка',
        'erase,стереть',
        'field,область',
        'filetype,типфайла',
        'fontsize,размершрифта',
        'foreground,переднийплан',
        'formfeed,подачаформы',
        'formatter,форматирован',
        'freeware,бесплатно',
        'grid,сетка',
        'hardlink,прямаяссылка',
        'hyperlink,гиперссылка',
        'input,ввод',
        'insert,вставка',
        'instant,мгновенное',
        'interrupt,прервать',
        'italictype,курсив',
        'jobscheduling,планирраб',
        'join,соединение',
        'justification,выравпошир',
        'landscapemode,горизонтальный',
        'lifetime,срокслужбы',
        'login,войтивсистему',
        'logout,выйтиизсистемы',
        'manual,руководство',
        'memorymap,картапамяти',
        'menubar,панельменю',
        'merge,слияние',
        'mirror,зеркало',
        'network,сеть',
        'next,следующий',
        'node,узел',
        'openafile,откройтефайл',
        'opensource,открист',
        'opticalfiber,оптволокно',
        'output,выход',
        'partition,разделение',
        'patch,патч',
        'path,путь',
        'portable,портативный',
        'postscript,постскриптум',
        'prompt,подсказка',
        'proxygateway,прокси',
        'pushbutton,нажатькнопку',
        'push-downlist,ниспадспис',
        'reboot,перезагрузка',
        'recovery,восстановление',
        'redirect,переадресовать',
        'redo,сделатьзаново',
        'reset,сброс',
        'router,маршрутизатор',
        'save,сохранить',
        'scan,просмотр',
        'scroll,прокрутка',
        'searchengine,поисковаямашина',
        'set,набор',
        'shareware,усл-беспл',
        'signoff,отписаться',
        'signon,подписаться',
        'smallletter,строчнаябуква',
        'smileyface,смайлик',
        'snapshot,снимок',
        'software, програмбеспеч',
        'sourcecode,исходныйтекст',
        'storage,хранение']

    word = random.randint(0, len(words) - 1)

    start = timer()

    # windows = Tk()
    # windows.geometry("450x200")

    # x2 = Label(windows, text=words[word], font="times 20")
    # x2["text"] = ""
    # x2.destroy()
    x2 = Label(windows, text=words[word] + "                         ", font="times 20")
    # x2.pack()

    # x2.config(text="")
    x2.place(x=140, y=10)

    x3 = Label(windows, text="Печатать EN и RU =>", font="times 20")
    x3.place(x=10, y=50)

    entry = Entry(windows)
    entry.place(x=280, y=55)
    ####windows = Tk()
    windows.geometry("450x200")
    entry.bind("<Return>", check_result)
    # Привязываем функцию check_result() к событию нажатия клавиши Enter в поле ввода

    entry.focus_set()  # Установка фокуса на поле ввода

    b2 = Button(windows, text="Проверка", command=check_result, width=12, bg='grey')
    b2.place(x=150, y=100)

    b3 = Button(windows, text="NEXT text", command=game, width=12, bg='grey')
    b3.place(x=250, y=100)

    # print (entry.focus_get())
    # entry.focus_set()  # 2222Установка фокуса на поле ввода
    # print (entry.focus_get())
    windows.mainloop()


x = 0
windows = Tk()
windows.geometry("450x200")
# window = Tk()
# window.geometry("450x200")

# x1 = Label(window, text="Начнем слепой ввод..", font="times 20")
# x1.place(x=10, y=50)

# b1 = Button(window, text="Go", command=game, width=12, bg='grey')
# b1.place(x=150, y=100)

# window.mainloop()


game()
