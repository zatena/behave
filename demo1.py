from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
# driver.get("https://www.baidu.com")
# driver.implicitly_wait(10)
#
# js = 'window.open("");'
# driver.execute_script(js)
#
# driver.get("https://www.tezign.com")


browser.get('https://www.tezign.com')

# 获取当前窗口句柄（窗口A）
handle = browser.current_window_handle

# 打开一个新的窗口
js = 'window.open("");'
browser.execute_script(js)

# 获取当前所有窗口句柄（窗口A、B）
handles = browser.window_handles

# 对窗口进行遍历
for newhandle in handles:
    # 筛选新打开的窗口B
    if newhandle!=handle:
        # 切换到新打开的窗口B
        # browser.switch_to_window(newhandle) 旧版本
        browser.switch_to.window(newhandle)

        # 在新打开的窗口B中操作
        browser.get('https://www.baidu.com')

        # 关闭当前窗口B
        browser.close()

        #切换回窗口A
        browser.switch_to.window(handles[0])