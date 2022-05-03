from selenium import webdriver
import time
import pyautogui
import pyperclip

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
browser = webdriver.Chrome("D:\RPA (python)\chromedriver.exe")
browser.implicitly_wait(10) # 페이지가 로딩될때까지 최대 10초 기다려줌
browser.maximize_window() # 화면 최대화
browser.get(url) # 페이지 열기

# 아이디 입력창
id = browser.find_element_by_css_selector("#id") # #id는 웹페이지 f12 눌러서 확인된 selector
id.click()
# id.send_keys("gold7942feel")
pyperclip.copy("gold7942feel")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 비밀번호 입력창
pw = browser.find_element_by_css_selector("#pw")
pw.click()
# pw.send_keys("qnfanfl@71")
pyperclip.copy("qnfanfl@71")
pyautogui.hotkey("ctrl","v")
time.sleep(2)

# 로그인 버튼 
login_btn = browser.find_element_by_css_selector("#log\.login")
login_btn.click()