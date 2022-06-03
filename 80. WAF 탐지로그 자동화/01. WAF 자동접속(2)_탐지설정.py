from selenium import webdriver
import time
import pyautogui
import pyperclip

# 수동으로 관리도구 창 최대화 이후 작업
# 탐지로그 이동
pyautogui.moveTo(2081,90)
pyautogui.click()
time.sleep(1)

# 기간 설정
pyautogui.moveTo(474,289)
pyautogui.click()
time.sleep(1)

# 사용자 정의 클릭
pyautogui.moveTo(442,514)
pyautogui.click()
time.sleep(1)