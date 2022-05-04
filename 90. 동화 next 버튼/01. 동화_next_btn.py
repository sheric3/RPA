import pyautogui
import time

# #1. 화면 크기 출력
# print(pyautogui.size()) #Size(width=2560, height=1440)

# # 4. 마우스  클릭
# pyautogui.click() #왼쪽 클릭
# pyautogui.click(button = 'right') #우클릭
# pyautogui.doubleClick() #더블클릭
# pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다 클릭

# 3. 마우스 이동
# for loop
for i in range(100000000):
    # 다음 편 선택
    time.sleep(2)
    pyautogui.moveTo(3967, 847)
    pyautogui.click()
    time.sleep(210) # 3분 30초

    # next 선택
    pyautogui.moveTo(4987,1218)
    pyautogui.click()
    # time.sleep(210) # 3분 30초


# 5. 마우스 드래그
# pyautogui.moveTo(1738,51,2)
# pyautogui.dragTo(1616,54,2)