import pyautogui
import time
import pyperclip
import tkinter as tk
from pynput import keyboard
from PIL import Image, ImageTk
# 마우스 포지션찾기
# print(pyautogui.position())

# 가장 먼저 가격을 수동으로 설정해주셔야합니다.
# Point(x=1664, y=391) = 4% 매수매도
# x=521, y=748) = 50%

sleepTime = 0.03


def buySell100PercentageSetting():
    print(pyautogui.moveTo(1902, 396))
    print(pyautogui.moveTo(1902, 390, 0.2))
    time.sleep(sleepTime)
    pyautogui.click()
    # time.sleep(sleepTime)


def buySell4PercentageSetting():
    print(pyautogui.moveTo(x=1664, y=391))
    pyautogui.click()
    time.sleep(sleepTime)


def leverageButtonClick(leverage):
    # ----------------------
    # 배수 조정 클릭
    print(pyautogui.moveTo(197, 197))
    pyautogui.click()
    time.sleep(0.3)

    # 배수 조정 클릭
    # print(pyautogui.moveTo(956, 500))
    # pyautogui.click(949, 468)
    x, y = pyautogui.locateCenterOnScreen('binance_leverage.png')
    print(x, y)
    pyautogui.click(x-60, y)

    time.sleep(sleepTime)

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(str(leverage))
    time.sleep(0.4)

    # if times < 0:
    #     for i in range(-times):
    #         # 배수 한칸 마이너스 조정 클릭
    #         print(pyautogui.moveTo(817, 498))
    #         pyautogui.click()
    #         # time.sleep(0.001)
    # else:
    #     for i in range(times):
    #         # 배수 한칸 마이너스 조정 클릭
    #         print(pyautogui.moveTo(1095, 498))
    #         pyautogui.click()
    #         # time.sleep(0.001)

    # 확인 클릭
    # print(pyautogui.moveTo(1039, 737))
    # pyautogui.click(1042, 707)
    x, y = pyautogui.locateCenterOnScreen('test.png')
    # print(x, y)
    pyautogui.click(x, y)
    time.sleep(sleepTime+0.9)

    # ----------------------


def reduceOnlyUpper():
    # print(pyautogui.moveTo(x=1655, y=578))
    pyautogui.click(1655, y=578)
    time.sleep(sleepTime)


def reduceOnlyLower():
    # print(pyautogui.moveTo(1652, 601))
    pyautogui.click(1652, 601)
    time.sleep(sleepTime)


def buyButtonClick():
    # print(pyautogui.moveTo(1711, y=656))
    pyautogui.click(1711, y=638)
    time.sleep(sleepTime)


def sellButtonClick():
    print(pyautogui.moveTo(1842, 638))
    pyautogui.click()
    time.sleep(sleepTime)


def bitcoinPriceSetting(price):
    pyautogui.click(1770, 316)
    pyautogui.click(1770, 316)
    time.sleep(0.03)
    # pyautogui.hotkey('ctrl', 'a')
    # time.sleep(1)
    pyautogui.typewrite(str(price))


def earnCutFunc(price, earnCut, sellOrBuy):
    pyautogui.click(1795, 479)
    pyautogui.click(1795, 479)
    if sellOrBuy == "buy":
        tmp = float(price)*(1+float(earnCut)/100)+0.45
        # pyautogui.hotkey('ctrl', 'a')
        # pyautogui.typewrite(str(tmp))
    else:
        tmp = float(price)*(1-float(earnCut)/100)+0.45
        # pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(str(tmp))
    time.sleep(0.05)
    print(tmp)


def lossCutFunc(price, lossCut, sellOrBuy):
    pyautogui.click(1795, 519)
    pyautogui.click(1795, 519)
    if sellOrBuy == "buy":
        tmp = float(price)*(1-float(lossCut)/100)+0.45
        # pyautogui.hotkey('ctrl', 'a')
    else:
        tmp = float(price)*(1+float(lossCut)/100)+0.45
    pyautogui.typewrite(str(tmp))
    time.sleep(0.05)
    print(tmp)


def buySummary(price, leverage=0, reduceClick=0, earnCut=None, lossCut=None):
    bitcoinPriceSetting(float(price)+0.45)
    print(price, leverage, reduceClick, earnCut, lossCut)
    if reduceClick:
        reduceOnlyUpper()
    if leverage and leverage != '0':
        leverageButtonClick(leverage)
    if earnCut:
        earnCutFunc(price, earnCut, "buy")
    if lossCut:
        lossCutFunc(price, lossCut, "buy")
    buySell100PercentageSetting()
    buyButtonClick()


def sellSummary(price, leverage=0, reduceClick=1, earnCut=None, lossCut=None):
    print(price, leverage, reduceClick)
    if reduceClick:
        reduceOnlyUpper()
    if leverage and leverage != '0':
        leverageButtonClick(leverage)
    bitcoinPriceSetting(float(price)+0.45)
    if earnCut:
        earnCutFunc(price, earnCut, "sell")
    if lossCut:
        lossCutFunc(price, lossCut, "sell")
    buySell100PercentageSetting()
    sellButtonClick()


# buySummary(59735.5, leverage=0, reduceClick=1)
# buySummary(58357.5, 100, 0)
# sellSummary(60445.8, 0)


def tkinterVisual():
    # def print_selection():

    # if (var1.get() == 1) & (var2.get() == 0):
    #     l.config(text='I love Python ')
    # elif (var1.get() == 0) & (var2.get() == 1):
    #     l.config(text='I love C++')
    # elif (var1.get() == 0) & (var2.get() == 0):
    #     l.config(text='I do not anything')
    # else:
    #     l.config(text='I love both')

    master = tk.Tk()
    master.title("바이낸스 주문")
    tk.Label(master,
             text="주문 가격(달러)").grid(row=0)

    tk.Label(master,
             text="레버리지").grid(row=1)
    tk.Label(master,
             text="익절%").grid(row=2)
    tk.Label(master,
             text="손절%").grid(row=3)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    var1 = tk.IntVar()
    c1 = tk.Checkbutton(master, text='reduceOnly 체크', variable=var1,
                        onvalue=1, offvalue=0)
    # c1.pack()

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    c1.grid(row=4, column=1)
    tk.Button(master,
              text='매수',
              command=lambda: buySummary(e1.get(), e2.get(), var1.get(), e3.get(), e4.get())).grid(row=5,
                                                                                                   column=0,
                                                                                                   sticky=tk.W,
                                                                                                   pady=4)
    tk.Button(master,
              text='매도', command=lambda: sellSummary(e1.get(), e2.get(),  var1.get(), e3.get(), e4.get())).grid(row=5,
                                                                                                                column=1,
                                                                                                                sticky=tk.W,
                                                                                                                pady=4)
    # tk.Button(master,
    #           text='레버리지',
    #           command=lambda: cancelOrder(1)).grid(row=3,
    #                                                column=2,
    #                                                sticky=tk.W,
    #                                                pady=4)

    # tk.Button(master,
    #           text='주문 취소',
    #           command=lambda: cancelOrder(1)).grid(row=3,
    #                                                column=2,
    #                                                sticky=tk.W,
    #                                                pady=4)

    tk.mainloop()


tkinterVisual()
