# encoding: utf-8
from behave import *
from features.utils.seleniumapi import SeleniumApi
import time
from features.utils.exceptioncatch import ExceptionCatch


@given('在后台首页')
def step_open(content):
    time.sleep(1)


@when('找到用户管理')
def step_click_user_management(content):
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[1]/div/div/div/ul/li[3]/div/span/span')
    time.sleep(1)


@then('找到发现库内创意方')
def step_find_innerdesigner(content):
    if '发现库内创意方' in SeleniumApi.step_text_xpath(content, '//*[@id="subMenu-3$Menu"]/li[3]'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False


@when('点击发现库内创意方')
def step_click_innerdesigner(content):
    SeleniumApi.step_click(content, '//*[@id="subMenu-3$Menu"]/li[3]')
    time.sleep(5)


@then('显示发现库内创意方页面')
def step_check_innderdesigner(content):
    if '个案例符合条件' in SeleniumApi.step_text_xpath(content, '//*[@id="rc-root"]/div/div[3]/div/div/div/div[3]/div[1]/'
                                                         'div[2]/div[3]/div[1]/div[2]/div[2]/div[2]/span'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False


@when('关键词搜索')
def step_keywords_search(content):
    SeleniumApi.step_send_keys(content, '//*[@id="rc-root"]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/'
                                        'div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div/ul/li/div/input','插画')
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/'
                                        'div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div/div/div/ul/li/div/input')
    time.sleep(1)
    SeleniumApi.step_click(content, '/html/body/div[2]/div/div/div/ul/li[1]/ul/li[1]')
    time.sleep(1)
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]'
                                    '/div[1]/div[2]/div[7]/div/button[1]')


@then('校验搜索结果')
def step_verify_search_result(content):
    if '特赞插画作品' in SeleniumApi.step_text_xpath(content, '//*[@id="rc-root"]/div/div[3]/div/div/div/div[3]/div[1]'
                                                        '/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[1]/div/div[2]'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False
    time.sleep(3)


@when('点击任一案例查看详情')
def step_click_portfolio(content):
    SeleniumApi.step_click(content, '//*[@id="rc-root"]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/'
                                    'div[2]/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[1]')
    time.sleep(3)
    ExceptionCatch.catch_exception(content)


@then('案例展示正常')
def step_portfolio_ok(content):
    SeleniumApi.step_switch_to_a_tab(content)
    time.sleep(1)
    if '案例详情' in SeleniumApi.step_text_xpath(content, '//*[@id="rc-root"]/div/div[3]/div/div/div[1]/span[1]'):
        assert True
    else:
        ExceptionCatch.catch_exception(content)
        assert False




