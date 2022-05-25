import pyautogui
import time
import tkinter

# # 4. 마우스  클릭
# pyautogui.click() #왼쪽 클릭
# pyautogui.click(button = 'right') #우클릭
# pyautogui.doubleClick() #더블클릭
# pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다 클릭

# 3. 마우스 이동
# for loop

for i in range(100000000):
    # 다음 편 선택
    pyautogui.moveTo(4585, 395)
    pyautogui.click()

    #
    pyautogui.moveTo(5012, 565)
    time.sleep(1)
    pyautogui.click()
    # 마우스 모니터 중앙 두기
    pyautogui.moveTo(1469, 554)

    # time.sleep(210)  # 3분 30초
    # time.sleep(240)  # 4분
    time.sleep(180) # 3분
    # time.sleep(150)  # 2분 30초
    # time.sleep(120)  # 2분

    # # next 선택
    # pyautogui.moveTo(4987,1218)
    # pyautogui.click()
    # # time.sleep(210) # 3분 30초

    # # 마우스 모니터 중앙 두기
    # pyautogui.moveTo(1469,554)

# 5. 마우스 드래그
# pyautogui.moveTo(1738,51,2)
# pyautogui.dragTo(1616,54,2)