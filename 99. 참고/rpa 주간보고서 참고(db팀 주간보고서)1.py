from selenium import webdriver
import time, datetime
import os, shutil
from PIL import Image


def start_sherpa():
    today = datetime.datetime.today()
    st_date = today - datetime.timedelta(7)
    st_date = st_date.strftime('%Y.%m.%d')
    en_date = today - datetime.timedelta(1)
    en_date = en_date.strftime('%Y.%m.%d')
    todayd = today.strftime('%Y.%m.%d')
    today = today.strftime('%Y%m%d')
    path = '/home/seonglf/img/'

    if os.path.exists(path + today):
        shutil.rmtree(path + today)
    if not os.path.exists(path + today):
        os.makedirs(path + today)
    path = path + today + '/'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # crawling
    driver = webdriver.Chrome(executable_path="/home/seonglf/chromedriver", chrome_options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.get('http://10.1.123.85:8080/sherpa-web/oracle/logAnalysis/timeBase.do')
    driver.implicitly_wait(10)
    time.sleep(3)
    driver.find_element_by_id('product').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[1]/ul/li[1]').click()
    driver.find_element_by_xpath('//*[@id="userId"]').send_keys('sherpa')
    driver.find_element_by_xpath('//*[@id="userPwd"]').send_keys('1')
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/p[4]/button').click()
    driver.find_element_by_xpath('/html/body/div/div[1]/div/img[3]').click()
    driver.implicitly_wait(5)

    def get_performanceTrend():
        driver.find_element_by_class_name('from_date').clear()
        driver.find_element_by_class_name('from_date').send_keys(st_date)
        driver.find_element_by_class_name('to_date').clear()
        driver.find_element_by_class_name('to_date').send_keys(en_date)
        driver.find_element_by_class_name('to_hours_selectbox').send_keys('23')
        # 아무데나 클릭
        # driver.find_element_by_class_name('orcl_overALL_CpuDiv_AVG').click()
        driver.find_element_by_class_name('logo').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/form/div[1]/div[1]/div[4]/div/button').click()
        time.sleep(3)
        driver.implicitly_wait(1)
        driver.find_element_by_id('cpuWait_orcl_overAll_CpuChart').click()
        time.sleep(1)
        img = driver.find_element_by_xpath('//*[@id="logSearchForm"]/div[2]').screenshot_as_png
        with open(path + '3. Performance Trend.png', 'wb') as file:
            file.write(img)

    # top n
    def get_topQuery():
        driver.find_element_by_class_name('logAnalysis').click()
        driver.find_element_by_xpath('/html/body/div[1]/header/div/nav/ul/li[3]/div/div[1]/ul[1]/li[2]/p').click()
        time.sleep(2)
        driver.find_element_by_class_name('from_date').clear()
        driver.find_element_by_class_name('from_date').send_keys(st_date)
        driver.find_element_by_class_name('to_date').clear()
        driver.find_element_by_class_name('to_date').send_keys(en_date)
        driver.find_element_by_class_name('to_hours_selectbox').send_keys('23')
        # 아무데나 클릭
        driver.find_element_by_class_name('logo').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div/div/form/div[1]/div/div[6]/div/button').click()
        time.sleep(2)
        driver.find_element_by_id('item').click()
        driver.find_element_by_id('criteria2').click()
        time.sleep(1)
        img = driver.find_element_by_xpath('//*[@id="gview_orcl_period_catagory"]').screenshot_as_png
        with open(path + '9. Physical Reads top10.png', 'wb') as file:
            file.write(img)

        driver.find_element_by_id('item').click()
        driver.find_element_by_id('criteria4').click()
        time.sleep(1)
        img = driver.find_element_by_xpath('//*[@id="gview_orcl_period_catagory"]').screenshot_as_png
        with open(path + '7. Execute Count top10.png', 'wb') as file:
            file.write(img)

        driver.find_element_by_id('item').click()
        driver.find_element_by_id('criteria7').click()
        time.sleep(1)
        img = driver.find_element_by_xpath('//*[@id="gview_orcl_period_catagory"]').screenshot_as_png
        with open(path + '8. Elapsed Time top10.png', 'wb') as file:
            file.write(img)

    def get_HeatmapTrend():
        driver.find_element_by_class_name('logAnalysis').click()
        driver.find_element_by_class_name('resourceHeatmap').click()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name('from_date').clear()
        driver.find_element_by_class_name('from_date').send_keys(st_date)
        driver.find_element_by_class_name('to_date').clear()
        driver.find_element_by_class_name('to_date').send_keys(en_date)
        driver.find_element_by_xpath('//*[@id="selectitem"]/button[6]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="orcl_filter"]').click()
        driver.find_element_by_xpath('//*[@id="itemBox"]/ul/li[2]').click()

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="logSearchForm"]/div[1]/div/div[5]/button').click()
        time.sleep(2)
        img = driver.find_element_by_xpath('//*[@id="logSearchForm"]/div[2]/div[1]').screenshot_as_png
        with open(path + '4. Heatmap Trend.png', 'wb') as file:
            file.write(img)

    def get_allSessionFlow():
        driver.find_element_by_class_name('logAnalysis').click()
        # driver.find_element_by_id('ui-id-13').clear()
        driver.find_element_by_xpath('//*[@id="ui-id-13"]').click()
        time.sleep(1)
        driver.find_element_by_class_name('allSessionFlow').click()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name('from_date').clear()
        driver.find_element_by_class_name('from_date').send_keys(st_date)
        driver.find_element_by_class_name('to_date').clear()
        driver.find_element_by_class_name('to_date').send_keys(en_date)
        driver.find_element_by_class_name('to_hours_selectbox').send_keys('23')
        driver.find_element_by_class_name('logo').click()
        driver.find_element_by_xpath('//*[@id="orcl_searchAllSessionFlow"]').click()
        driver.find_element_by_id('CategorySelect').click()
        driver.find_element_by_xpath('//*[@id="CategorySelect"]/option[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('logo').click()
        img = driver.find_element_by_xpath('//*[@id="logSearchForm"]/div[2]/div[1]/div').screenshot_as_png
        with open(path + '5. All Session Flow.png', 'wb') as file:
            file.write(img)

    def get_tablespaceUsage():
        driver.find_element_by_class_name('logAnalysis').click()
        driver.find_element_by_xpath('//*[@id="ui-id-15"]').click()
        time.sleep(1)
        driver.find_element_by_class_name('tablespaceUsage').click()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name('from_date').clear()
        driver.find_element_by_class_name('from_date').send_keys(st_date)
        driver.find_element_by_class_name('to_date').clear()
        driver.find_element_by_class_name('to_date').send_keys(en_date)
        driver.find_element_by_xpath('//*[@id="sherpaMessageOkBtn"]').click()
        driver.find_element_by_xpath('//*[@id="orcl_searchTablespaceUsage"]').click()
        time.sleep(1)
        img = driver.find_element_by_xpath('//*[@id="logSearchForm"]/div[2]/div/div[1]/div[1]').screenshot_as_png
        with open(path + '1. Tablespace Usage.png', 'wb') as file:
            file.write(img)

    def get_filesystemUsage():
        driver.find_element_by_class_name('logAnalysis').click()
        driver.find_element_by_xpath('//*[@id="ui-id-15"]').click()
        time.sleep(1)
        driver.find_element_by_class_name('filesystemUsage').click()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name('from_date').clear()
        driver.find_element_by_class_name('from_date').send_keys(st_date)
        driver.find_element_by_class_name('to_date').clear()
        driver.find_element_by_class_name('to_date').send_keys(en_date)
        driver.find_element_by_class_name('to_hours_selectbox').send_keys('23')
        driver.find_element_by_class_name('logo').click()
        driver.find_element_by_xpath('//*[@id="orcl_searchFilesystemUsage"]').click()
        time.sleep(3)
        img = driver.find_element_by_xpath('//*[@id="gview_orcl_filesystemUsageList"]').screenshot_as_png
        with open(path + '2. Filesystem Usage.png', 'wb') as file:
            file.write(img)
        img = Image.open(path + '2. Filesystem Usage.png')
        img = img.crop((0, 0, 1546, 165))
        img.save(path + '2. Filesystem Usage.png')

    def get_categoryPerformance():
        driver.find_element_by_class_name('logAnalysis').click()
        driver.find_element_by_xpath('//*[@id="ui-id-12"]/li[4]/p').click()
        time.sleep(2)
        driver.find_element_by_class_name('from_date').clear()
        driver.find_element_by_class_name('from_date').send_keys(st_date)
        driver.find_element_by_class_name('to_date').clear()
        driver.find_element_by_class_name('to_date').send_keys(en_date)
        driver.find_element_by_class_name('to_hours_selectbox').send_keys('23')
        # 아무데나 클릭
        driver.find_element_by_class_name('logo').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="logSearchForm"]/div[1]/div[1]/div[6]/div/button').click()
        time.sleep(3)
        img = driver.find_element_by_xpath('//*[@id="viewTab_orcl"]').screenshot_as_png
        with open(path + '6. Category Performance.png', 'wb') as file:
            file.write(img)

    get_performanceTrend()
    get_topQuery()
    get_HeatmapTrend()
    get_allSessionFlow()
    get_categoryPerformance()
    get_filesystemUsage()
    get_tablespaceUsage()
    print('complete save images ' + time.strftime('%H' + ':' + '%M' + ':' + '%S'))

    driver.close


start_sherpa()

