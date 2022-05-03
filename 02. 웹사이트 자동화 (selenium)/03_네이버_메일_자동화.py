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
time.sleep(2)

# 메일함  이동
browser.get("https://mail.naver.com/")
time.sleep(2)

# 메일 쓰기 버튼
browser.find_element_by_css_selector("#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault > strong > span").click()
time.sleep(2)

# 받는사람 입력 #interval 은 사람이 입력하는 것처럼 한글자씩 입력됨
pyautogui.write("gold7942feel@naver.com", interval=0.25)
pyautogui.press('enter') 
pyautogui.press("tab") # 탭 이동
pyautogui.press("tab") # 탭 이동
time.sleep(2)

# 제목 입력
pyperclip.copy("파이썬에서 자동으로 보낸 메일입니다.")
pyautogui.press('enter')
pyautogui.hotkey("ctrl", 'v')

# 본문 입력
pyautogui.press("tab") # 탭 이동
time.sleep(2)
pyperclip.copy("본문 내용 작성 신기하죠?")
pyautogui.hotkey("ctrl", 'v')

# 보내기 버튼 클릭
browser.find_element_by_css_selector("#sendBtn").click()