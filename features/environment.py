# encoding: utf-8
from selenium import webdriver
from features.utils.seleniumapi import SeleniumApi
from features.utils.exceptioncatch import ExceptionCatch
import time
import os
import shutil


if os.path.exists('./report'):
    shutil.rmtree('./report')
    os.mkdir('./report')

else:
    os.mkdir('./report')


def before_feature(content, feature):
    content.driver = webdriver.Chrome()
    content.driver.get("https://tezign:e071fc62bfc06c02abe0ec27@top.tezign.com")
    content.driver.implicitly_wait(10)
    content.driver.maximize_window()
    time.sleep(1)
    SeleniumApi.step_send_keys(content, "//*[@placeholder='邮箱']", 'zhengjingjing@tezign.com')
    time.sleep(1)
    SeleniumApi.step_send_keys(content, "//*[@placeholder='密码']", '111111')
    SeleniumApi.step_click(content, "//*[@type='button']")
    if '特赞基地' == SeleniumApi.step_text_cssselector(content, ".side-header"):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False


def after_feature(content, feature):
    content.driver.quit()
