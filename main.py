import time

import pyautogui
from numpy import where
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True
i = 1

while i<300:
    print("\033[1;34m"f"进入第{i}次操作")
    t1 = pyautogui.locateOnScreen('1/t1.png', confidence=0.8)
    if t1 is not None:
        x, y = pyautogui.center(t1)
        xx,yy = x+190,y+10
        pyautogui.leftClick(xx, yy)
        print("\033[1;32m""点击")
        time.sleep(1)

    t2 = pyautogui.locateOnScreen('1/t2.png', confidence=0.8)
    t22 = pyautogui.locateOnScreen('1/t22.png', confidence=0.8)
    if t2 is not None:
        x, y = pyautogui.center(t2)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""点击")
        time.sleep(3)
    elif t22 is not None:
        x, y = pyautogui.center(t22)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""点击")
        time.sleep(3)




    r1 = pyautogui.locateOnScreen('1/1.png', confidence=0.5)
    if r1 is not None:
        x,y = pyautogui.center(r1)
        pyautogui.leftClick(x,y)
        print("\033[1;32m""点击菜单")
        time.sleep(1)
    else:
        print("\033[1;31m"'未发现1，菜单')

    r2 = pyautogui.locateOnScreen('1/2.png', confidence=0.8)
    if r2 is not None:
        x, y = pyautogui.center(r2)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""点击跳过")
        time.sleep(1)
    else:
        print("\033[1;31m"'未发现2，跳过')

    r3 = pyautogui.locateOnScreen('1/3.png', confidence=0.8)
    if r3 is not None:
        x, y = pyautogui.center(r3)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""点击OK")
        time.sleep(6)
    else:
        print("\033[1;31m"'未发现3，OK')

    r4 = pyautogui.locateOnScreen('1/4.png', confidence=0.8)
    r44 = pyautogui.locateOnScreen('1/44.png', confidence=0.8)
    if r4 is not None:
        x, y = pyautogui.center(r4)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""轻触继续")
        time.sleep(1)
    elif r44 is not None:
        x, y = pyautogui.center(r44)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""进入战斗，等待20秒")
        time.sleep(20)
        k = 0
        while k<1:
            r444 = pyautogui.locateOnScreen('1/444.png', confidence=0.8)
            r4444 = pyautogui.locateOnScreen('1/4444.png', confidence=0.8)
            #c = 0
            if r444 is not None:
                x, y = pyautogui.center(r444)
                pyautogui.leftClick(x, y)
                print("\033[1;32m""战斗结束")
                #c += 1
                k += 1
                time.sleep(3)
            elif r4444 is not None:
                x, y = pyautogui.center(r4444)
                pyautogui.leftClick(x, y)
                print("\033[1;32m""战斗失败")
                time.sleep(3)
                pyautogui.leftClick(x, y)
                #c += 1
                k += 1
                time.sleep(3)
            else:
                print("未检测到画面")
            #k = c
    else:
        print("\033[1;31m"'未发现4&44，结算和战斗')

    t3 = pyautogui.locateOnScreen('1/t3.png', confidence=0.8)
    if t3 is not None:
        x, y = pyautogui.center(t3)
        pyautogui.leftClick(x, y)
        print("\033[1;32m""进入下一节")
        pyautogui.leftClick(x, y)
        pyautogui.leftClick(x, y)
        time.sleep(3)
        pyautogui.leftClick(x+100, y)
        time.sleep(5)
    else:
        print("\033[1;31m"'未发现5')
    i += 1
