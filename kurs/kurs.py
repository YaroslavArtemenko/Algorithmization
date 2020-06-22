from math import *
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *



funcText = ''


functionLabelValue = None
numberLabelValue = None
errorLabel = None


def f(x):
    return eval(funcText)



def work(f, a, b, n):
    # print("\nТекущее число разбиений: ", n)
    h = (b - a) / float(n)
    # print("Текущий шаг:", h)
    total = sum([f((a + (k * h))) for k in range(0, n)])
    result = h * total
    # print("Текущий результат: ", result)
    return result



def main(f, a, b, eps):
    global functionLabelValue
    global numberLabelValue
    if (functionLabelValue):
        functionLabelValue.destroy()
    if (numberLabelValue):
        numberLabelValue.destroy()
    n = 2
    a1 = work(f, 1, 2, n)
    n *= 2
    a2 = work(f, 1, 2, n)

    while abs(a1 - a2) > eps:
        n *= 2
        a1 = work(f, a, b, n)
        n *= 2
        a2 = work(f, a, b, n)


    functionLabelValue = Label(text=f'Відповідь: F(x)={a2}')
    functionLabelValue.pack()
    numberLabelValue = Label(text=f'Кількість розбиттів: N ={n}')
    numberLabelValue.pack()


    f2 = np.vectorize(f)
    x = np.linspace (-10, 10, 100)

    plt.plot(x, f2(x))
    plt.plot(a)
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(True)
    plt.ylim(-10, 10)



    plt.show()


    return a2



window = Tk()
window.title('Метод лівих прямокутників')
window.geometry("350x300")


functionLabel = Label(text='Введіть функцію f(x): ',
                      font = ("Times New Roman", 13))
functionLabel.pack()

combo = Combobox(window, width = 27)
combo['values'] = ('exp(1/x)/(x*x)', '1/x', 'x**2')
combo.pack()


startPointLabel = Label(text='Введіть початкове значення "а": ',
                      font = ("Times New Roman", 13))
startPointValue = Entry(window, width = 30)

startPointLabel.pack()
startPointValue.pack()

endPointLabel = Label(text='Введіть кінцеве значення "b": ',
                      font = ("Times New Roman", 13))
endPointValue = Entry(window, width = 30)

endPointLabel.pack()
endPointValue.pack()

epsLabel = Label(text='Введіть похибку "E": ',
                      font = ("Times New Roman", 13))
epsValue = Entry(window, width = 30)

epsLabel.pack()
epsValue.pack()

label_1 = Label(text='\n')
label_1.pack()


def submitForm():
    global errorLabel
    if(errorLabel):
        errorLabel.destroy()
    if (functionLabelValue):
        functionLabelValue.destroy()
    if (numberLabelValue):
        numberLabelValue.destroy()
    try:

        global funcText
        global a
        global b
        global eps
        global f
        funcText = combo.get()
        print (funcText)

        try:
            a = float(startPointValue.get())
            print (a)
        except:
            errorLabel = Label(text='Помилка в нижній межі "а"', foreground = "#f00")
            errorLabel.pack()
            return None

        try:
            b = float(endPointValue.get())
            print (b)
        except:
            errorLabel = Label(text = 'Помилка в верхній межі "b"', foreground = "#f00")
            errorLabel.pack()
            return None

        try:
            eps = float(epsValue.get())
            print(eps)
        except:
            errorLabel = Label(text = 'Помилка в точності', foreground = "#f00")
            errorLabel.pack()
            return None

        if (eps >= 1):
            errorLabel = Label(text='Точність має бути менше 1', foreground="#f00")
            errorLabel.pack()
            return None

        if (a >= b):
            errorLabel = Label(text='"а" повинно бути менше за "b"', foreground="#f00")
            errorLabel.pack()
            return None

        main(f, a, b, eps)
    except :#Exception as e:
        # print(traceback.format_exc())
        errorLabel = Label(text='Помилка в функції!', foreground = "#f00")
        errorLabel.pack()


submitButton = Button(window, text='Вирішити',
                      command=submitForm)
submitButton.pack()


window.mainloop()

