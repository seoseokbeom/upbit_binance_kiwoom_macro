import pyautogui
import time
import pyperclip
import tkinter as tk
from pynput import keyboard
from PIL import Image, ImageTk
from win32com.shell import shell

if shell.IsUserAnAdmin():
    print("관리자입니다.")
else:
    print("관리자가 아닙니다.")


sleepTime = 0.03


def changeTicker(ticker):
    pyautogui.click(653, 605)
    # time.sleep(0.03)
    pyautogui.click(29, 123)
    # pyautogui.click(189, 355)
    pyautogui.typewrite(str(ticker))
    time.sleep(0.03)
    pyautogui.press('enter')


def buyAmount(money):
    pyautogui.click(387, 153)
    pyautogui.click(189, 352)
    pyautogui.click(448, 240)
    pyautogui.click(button='right')
    pyautogui.press('c')
    time.sleep(sleepTime)
    price = pyperclip.paste().replace(',', '')
    # time.sleep(sleepTime)
    print(money, price, '--')
    amount = int(money*10000//(float(price)*1100))
    print(money*10000, float(price)*1100, amount)
    pyautogui.click(434, 197)
    pyautogui.typewrite(str(amount))
    pyautogui.click(551, 237)
    pyautogui.moveTo(397, 326)


def sellAmount(money):
    pyautogui.click(438, 153)
    pyautogui.click(189, 332)

    pyautogui.click(448, 240)
    pyautogui.click(button='right')
    pyautogui.press('c')

    # pyautogui.hotkey('ctrl', 'c')
    time.sleep(sleepTime)
    price = pyperclip.paste().replace(',', '')
    # time.sleep(sleepTime)
    print(money, price, '--')
    # btcCurrPrice = int(amount.replace(',', ''))
    amount = int(money*10000//(float(price)*1100))
    print(money*10000, float(price)*1100, amount)
    pyautogui.click(434, 197)
    pyautogui.typewrite(str(amount))
    pyautogui.click(551, 237)
    # pyautogui.click(444, 198)
    # pyautogui.typewrite(str(amount))
    # pyautogui.moveTo(920, 541)
    pyautogui.moveTo(397, 326)


def buyOrderSummary(ticker, krwMoney):
    changeTicker(ticker)
    buyAmount(krwMoney)


def sellOrderSummary(ticker, krwMoney):
    changeTicker(ticker)
    sellAmount(krwMoney)


# changeTicker("arkk")
# sellAmount(30)


def tkinterVisual():
    master = tk.Tk()
    master.title("키움 주문")
    tk.Label(master,
             text="티커").grid(row=0)

    tk.Label(master,
             text="주문금액(만원)").grid(row=1)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    tk.Button(master,
              text='매수',
              command=lambda: buyOrderSummary(e1.get(), float(e2.get()))).grid(row=3,
                                                                               column=0,
                                                                               sticky=tk.W,
                                                                               pady=4)
    tk.Button(master,
              text='매도', command=lambda: sellOrderSummary(e1.get(), float(e2.get()))).grid(row=3,
                                                                                           column=1,
                                                                                           sticky=tk.W,
                                                                                           pady=4)
    # tk.Button(master,
    #           text='주문 취소',
    #           command=lambda: cancelOrder(1)).grid(row=3,
    #                                                column=2,
    #                                                sticky=tk.W,
    #                                                pady=4)

    tk.mainloop()


tkinterVisual()
