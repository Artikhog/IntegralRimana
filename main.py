import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def selectFunction():
    global f
    if c == 0:
        f = lambda x: 5**x
    elif c == 1:
        f = lambda x: 5**(x + 0.5 * di)
    elif c == 2:
        f = lambda x: 5**(x + di)
    else:
        print("Ну ты и душнила. По умолчанию введено среднее оснащение. ")
        f = lambda x: 5 ** (x + 0.5 * di)


def summation():
    integralsum = 0
    for i in range(n):
        integralsum += f(s[i]) * di
        ax.add_patch(patches.Rectangle((s[i], 0), di, f(s[i]), edgecolor='blue', fill=False))
    print(integralsum)
    plt.title("Значение интегральной суммы = " + str(round(integralsum, 5)))
    plt.show()


def plotFunction():
    global ax, fig
    fig, ax = plt.subplots()
    x = np.linspace(0, math.pi)
    y = [5 ** i for i in x]
    ax.grid()
    plt.plot(x, y, 'r', label='line one', linewidth=1)
    plt.xlabel("ось X")
    plt.ylabel("ось Y")


def inputDivision():
    global n
    try:
        print("Введите количество точек разбиения:")
        n = int(input())
        if n < 0:
            print("Количество точек разбиения не может быть отрицательным. ")
            inputDivision()
    except:
        n = 20
        print("Ну ты и душнила. Введено разбиение по умолчанию. (n=20)")


def inputEquipment():
    global c
    try:
        print("Введите тип оснащения: 0-левое оснащение, 1-среднее оснащение, 2-правое оснащение:")
        c = int(input())
    except:
        c = 1
        print("Ну ты и душнила. По умолчанию введено среднее оснащение.")


def createDivision():
    global di, s
    di = math.pi / n
    s = [i * di for i in range(n)]


inputDivision()
inputEquipment()
createDivision()
selectFunction()
plotFunction()
summation()









