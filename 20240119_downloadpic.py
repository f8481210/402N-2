#匯入模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests

#宣告瀏覽器
c = webdriver.Chrome()

#到指定頁面
url = "https://pic.sogou.com/"
c.get(url)

time.sleep(0.5)

#搜尋輸入框
inputBar = c.find_element(By.CLASS_NAME,"query.query-defalut")
inputBar.send_keys("汪汪隊")

#按下鍵盤Enter
inputBar.send_keys(Keys.ENTER)

time.sleep(0.5)

#視窗放大
c.maximize_window()

time.sleep(0.5)
#往下滑
for i in range(2):
    c.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(0.5)

i = 1
#收集圖片網址
for e in c.find_elements(By.CSS_SELECTOR, 'img'):
    try:
        img_url = e.get_attribute('src') #圖片網址
        imgRespond = requests.get(img_url) #發送請求
        with open(str(i)+".jpg","wb") as file:
            file.write(imgRespond.content)
            print("done")
        if i == 30:
            break
        i+=1
    except:
        print("Failed")

c.close()







