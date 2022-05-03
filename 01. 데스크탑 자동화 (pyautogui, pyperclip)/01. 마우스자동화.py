import pyautogui
import time

# #1. 화면 크기 출력
# print(pyautogui.size()) #Size(width=2560, height=1440)

# # 2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position()) # Porint(x=2412, y=46)

# 3. 마우스 이동
#pyautogui.moveTo(1265, 250)
# pyautogui.moveTo(1265, 250, 2)

# # 4. 마우스  클릭
# pyautogui.click() #왼쪽 클릭
# pyautogui.click(button = 'right') #우클릭
# pyautogui.doubleClick() #더블클릭
# pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다 클릭

# 5. 마우스 드래그
pyautogui.moveTo(1738,51,2)
pyautogui.dragTo(1616,54,2)