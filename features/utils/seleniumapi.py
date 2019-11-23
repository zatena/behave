from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SeleniumApi:
    def step_click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def step_send_keys(self, xpath, xpath_value):
        self.driver.find_element_by_xpath(xpath).send_keys(xpath_value)

    def step_text_cssselector(self, cssselector):
        result = self.driver.find_element_by_css_selector(cssselector).text
        return result

    def step_text_xpath(self, xpath):
        result = self.driver.find_element_by_xpath(xpath).text
        return result

    def step_by_class(self, classname):
        self.driver.find_element_by_class_name(classname)

    def step_by_css(self, css):
        self.driver.find_element_by_css_selector(css)

    def step_wait_object(self, object):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, object)))

    def step_switch_to_alert(self, value1, value2):
        prompt = Alert(self.driver)
        prompt.send_keys(value1)
        prompt.send_keys(value2)
        prompt.accept()

    def step_switch_to_new_tab(self, newurl):
        # 获取当前窗口句柄（窗口A）
        handle = self.driver.current_window_handle
        
        # 打开一个新的窗口
        js = 'window.open("");'
        self.driver.execute_script(js)
        
        # 获取当前所有窗口句柄（窗口A、B）
        handles = self.driver.window_handles
        
        # 对窗口进行遍历
        for newhandle in handles:
            # 筛选新打开的窗口B
            if newhandle!=handle:
                # 切换到新打开的窗口B
                self.driver.switch_to.window(newhandle)
        
                # 在新打开的窗口B中操作
                self.driver.get(newurl)

    def step_switch_to_a_tab(self):
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles

        for newhandle in handles:
            if newhandle!=handle:
                self.driver.switch_to.window(newhandle)

    def step_switch_to_original_tab(self):
        handles = self.driver.window_handles
        # 关闭当前窗口B
        self.driver.close()

        # 切换回窗口A
        self.driver.switch_to.window(handles[0])

    def step_copy(self, css):
        self.driver.find_element_by_css_selector(css).send_keys(Keys.CONTROL,'c')

    def step_paste(self, css):
        self.driver.find_element_by_css_selector(css).send_keys(Keys.CONTROL,'v')

    def step_back(self):
        self.driver.back()

    def step_wait_expected(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))









