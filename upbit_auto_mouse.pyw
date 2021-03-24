# from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import pyautogui
import time
import pyperclip
import tkinter as tk
from pynput import keyboard
from PIL import Image, ImageTk
# from pynput.mouse import Listener
# from pynput.keyboard import Listener


def upperPriceClick():
    pyautogui.click(516, 526)


def lowerPriceClick():
    pyautogui.click(516, 569)


btcCurrPrice = 64502000
btc_amount = 0


def moneyToBtcAmount(money):

    pyautogui.click(1045, 307)
    time.sleep(0.02)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.02)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.02)
    amount = pyperclip.paste()
    # print(amount.replace(',', ''))
    time.sleep(0.02)
    btcCurrPrice = int(amount.replace(',', ''))
    # print(money, btcCurrPrice, money/btcCurrPrice*10000)
    return f"{(money+0.0001)/btcCurrPrice*10000:.9f}"

    # print(int(amount))
    # amount = int(pyperclip.paste().replace(',', ''))
    # print(amount)


def orderBtcAmount(btcAmount):
    pyautogui.click(1060, 355)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(str(btcAmount))


def sellCategoryClick():
    pyautogui.click(935, 178)


def buyCategoryClick():
    pyautogui.click(812, 178)


def finalOrderButtonClick():
    pyautogui.click(1050, 593)


def sellOrderSummary(krwAmount):
    sellCategoryClick()
    upperPriceClick()
    btcAmount = moneyToBtcAmount(float(krwAmount))
    orderBtcAmount(str(btcAmount))
    finalOrderButtonClick()
    x, y = pyautogui.locateCenterOnScreen('sellButton2.png')
    pyautogui.moveTo(x, y)
    # pyautogui.moveTo(1070, 635)


def buyOrderSummary(krwAmount):
    buyCategoryClick()
    lowerPriceClick()
    btcAmount = moneyToBtcAmount(float(krwAmount))
    orderBtcAmount(str(btcAmount))
    finalOrderButtonClick()
    # pyautogui.moveTo(1070, 635)
    x, y = pyautogui.locateCenterOnScreen('buyButton2.png')
    pyautogui.moveTo(x, y)


def cancelOrder(loopCnt=1):
    pyautogui.click(1180, 178)
    for _ in range(3):
        pyautogui.click(1209, 330)
        time.sleep(0.02)
        pyautogui.click(1070, 496)
        time.sleep(0.02)
        pyautogui.click(1070, 496)
        time.sleep(0.02)


def tkinterVisual():
    master = tk.Tk()
    master.title("업비트 주문")
    tk.Label(master,
             text="주문금액(만원)").grid(row=0)

    # tk.Label(master,
    #          text="Last Name").grid(row=1)

    e1 = tk.Entry(master)
    # e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    # e2.grid(row=1, column=1)

    tk.Button(master,
              text='매수',
              command=lambda: buyOrderSummary(e1.get())).grid(row=3,
                                                              column=0,
                                                              sticky=tk.W,
                                                              pady=4)
    tk.Button(master,
              text='매도', command=lambda: sellOrderSummary(e1.get())).grid(row=3,
                                                                          column=1,
                                                                          sticky=tk.W,
                                                                          pady=4)
    tk.Button(master,
              text='주문 취소',
              command=lambda: cancelOrder(1)).grid(row=3,
                                                   column=2,
                                                   sticky=tk.W,
                                                   pady=4)

    tk.mainloop()


# cancelOrder()
# sellOrderSummary(str(30.2))
# buyOrderSummary(str(5.2))
tkinterVisual()
