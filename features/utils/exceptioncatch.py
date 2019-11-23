import os
import time
from selenium import webdriver


picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))

if os.path.exists(os.getcwd()+'/screenshot'):
    print("截图文件夹已存在")
    pass
else:
    print("截图文件夹新建成功")
    os.mkdir(os.getcwd()+'/screenshot')

try:
    File_Path = os.getcwd() + '/screenshot/' + directory_time + '/'
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
        print("目录新建成功：%s" % File_Path)
    else:
        print("目录已存在！！！")
except BaseException as msg:
    print("新建目录失败：%s" % msg)


class ExceptionCatch():
    def catch_exception(self):
        try:
            self.driver.save_screenshot('./screenshot/' + directory_time + '/' + picture_time + '.png')
        except BaseException as pic_msg:
            print("截图失败：%s" % pic_msg)