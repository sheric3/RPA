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


