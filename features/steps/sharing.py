# encoding: utf-8
from behave import *
from features.utils.seleniumapi import SeleniumApi
import time
from features.utils.exceptioncatch import ExceptionCatch
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


@when('点开用户管理')
def step_click_user_management(content):
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[1]/div/div/div/ul/li[3]/div/span/span')
    time.sleep(1)


@then('找到分享列表管理')
def step_find_innerdesigner(content):
    if '分享列表' in SeleniumApi.step_text_xpath(content, '//*[@id="subMenu-3$Menu"]/li[5]'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False


@when('点击分享列表管理')
def step_click_sharinglist(content):
    SeleniumApi.step_click(content, '//*[@id="subMenu-3$Menu"]/li[5]')
    time.sleep(5)


@then('默认展示案例分享列表页面')
def step_check_portfolio(content):
    selected = SeleniumApi.step_text_xpath(content, '//*[@id="rc-root"]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
    locator = (By.XPATH, '//*[@id="rc-root"]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[1]')
    SeleniumApi.step_wait_expected(content, locator)

    if '案例分享列表' in selected:
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False


@when('指定标题搜索')
def step_keywords_search(content):
    SeleniumApi.step_send_keys(content, "//*[@placeholder='请输入标题']",'KV测试组案例')
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[1]/div/div/div[4]/'
                                    'div/button[1]')
    time.sleep(2)


@then('搜索结果正确')
def step_verify_search_result(content):
    if '1' == SeleniumApi.step_text_xpath(content, '//*[@id="rc-root"]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/'
                                                 'div[1]/p/span'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False


@when('点击分享')
def step_click_share(content):
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[3]/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/'
                                    'div[1]/div/div/div/div/div[2]/div/div/table/tbody/tr/td/span/button[1]')
    time.sleep(1)


@then('生成分享链接')
def step_new_sharinglink(content):
    if '分享链接已生成' in SeleniumApi.step_text_cssselector(content, '.modal-header'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False



@when('分享并查看分享内容')
def step_check_shareing(content):
    sharing_url = SeleniumApi.step_text_cssselector(content, '.link-detail')
    time.sleep(2)
    SeleniumApi.step_switch_to_new_tab(content, sharing_url)
    time.sleep(5)
    if '免费咨询' in SeleniumApi.step_text_xpath(content, '//*[@id="rc-root"]/div/div[2]/div/div[1]/div[3]/button'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div[1]')
    time.sleep(3)
    if '平台出品' in SeleniumApi.step_text_xpath(content, '/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/'
                                                      'div[1]/div/span'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
    ExceptionCatch.catch_exception(content)
    SeleniumApi.step_switch_to_original_tab(content)


@then('回到分享页面')
def step_back_to_sharing(content):
    if '分享链接已生成' in SeleniumApi.step_text_xpath(content, '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[1]'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False


@when('回到案例分享页面并退出系统')
def step_back_to_portfolio_group(content):
    SeleniumApi.step_back(content)
    time.sleep(1)
    SeleniumApi.step_click(content, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/span')
    SeleniumApi.step_click(content, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div/ul/li[2]/a')


@then('回到登录页面')
def step_back_to_loginpage(content):
    if 'We are the new sexy' in SeleniumApi.step_text_xpath(content, '//*[@id="rc-root"]/div/div/div[1]'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False