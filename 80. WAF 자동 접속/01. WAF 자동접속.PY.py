from selenium import webdriver
import time
import pyautogui
import pyperclip

pyautogui.moveTo(185, 859)
pyautogui.doubleClick()

# 시작 누르기
time.sleep(5)
pyautogui.moveTo(1248,485)
pyautogui.click()

# 아이디, 비번 입력
time.sleep(5)
pyautogui.moveTo(1365,690)
pyautogui.click()
pyautogui.write("shineric2202")
time.sleep(1)

pyautogui.moveTo(1357,720)
pyautogui.click()
pyautogui.write("!Q@W3e4r5t")
time.sleep(1)

pyautogui.moveTo(1359,786)
pyautogui.click()

# 탐지로그 이동
browser.maximize_window() # 화면 최대화
# pyautogui.moveTo(847,157)
# pyautogui.click()
# time.sleep(1)
#
# # 기간 설정
# pyautogui.moveTo(521,320)
# pyautogui.click()
# time.sleep(1)
#
# pyautogui.moveTo(463,546)
# pyautogui.click()
# time.sleep(1)
#
# # 기간 선택
# pyautogui.moveTo(99,177)
# pyautogui.click()
# time.sleep(1)
#
# pyautogui.moveTo(348,175)
# pyautogui.click()
# time.sleep(1)

