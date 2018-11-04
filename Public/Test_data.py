#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
需要安装第三方库
BeautifulSoup 解析Url获取apk下载链接地址
pip install beautifulsoup4

apkutils
A library that gets infos from APK.
https://github.com/mikusjelly/apkutils
pip install apkutils

"""
import os
import json
from Public.ReadConfig import ReadConfig

proDir = os.path.split(os.path.realpath(__file__))[0]
data_path = os.path.join(proDir, "data.json")


def generate_test_data(devices):
    dict_tmp = {}
    for d in devices:
        dict_tmp[d['serial']] = {}
        dict_tmp[d['serial']]['user_name'] = ReadConfig().get_testdata('user_name')[devices.index(d)]
        dict_tmp[d['serial']]['password'] = ReadConfig().get_testdata('password')[devices.index(d)]
    with open(data_path, "w") as f:
        json.dump(dict_tmp, f, ensure_ascii=False)
        f.close()
    print("Test data data.json generated success")


def get_test_data(d):
    with open(data_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data[d.device_info['serial']]


import requests
from bs4 import BeautifulSoup
import re
import apkutils
import json




def get_apk(url='http://www1.xiaoying.co/Android/vivavideo/vivavideo_install.html', keyword='xiaoyingtest'):
    '''
    :param url: url地址
    :param keyword: 匹配的关键字
    :return: 返回apk的参数url apk_name apk_path html
    '''
    folder = os.path.join(os.getcwd(), 'apk')
    print(folder)
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        pass
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "lxml")
    tmp = soup.find(href=re.compile(keyword))  # 获取下载链接
    apk = {'url': tmp.get('href'),
           'apk_name': tmp.get('href').split('/')[-1].replace(':', '_'),
           'apk_path': os.path.join(folder, tmp.get('href').split('/')[-1].replace(':', '_')),
           'html': tmp}
    return apk


def download_apk():
    apk = get_apk()
    print('from %s \ndownloading  %s ' % (apk['url'], apk['apk_name']))
    r = requests.get(apk['url'], 'wb')
    if r.status_code == 200:
        with open("%s" % (apk['apk_path']), "wb") as code:
            code.write(r.content)
        return True
    else:
        print('%s \nCannot GET ' % r.url)
        return False


def get_apk_info(path):
    tmp = apkutils.APK(path).get_manifest()
    info = {}
    info['versionCode'] = str(tmp.get('@android:versionCode'))
    info['versionName'] = str(tmp.get('@android:versionName'))
    info['package'] = str(tmp.get('@package'))
    return info


if __name__ == '__main__':
    # print(get_apk_url())
    # html = requests.get(url)
    # soup = BeautifulSoup(html.text,"lxml")
    # apk = soup.find(href=re.compile("xiaoyingtest"))
    # print(apk.text)
    # apk_url = apk.get('href')
    # print(apk_url)
    # print(download_apk())
    apk = get_apk()
    print(apk)

    # download_apk()
    # apk_info = get_apk_info(apk['apk_path'])
    # title = "自动化测试报告\nPackageName%s   Version:V%s  VersionCode:%s" % (
    #     apk_info["package"], apk_info["versionName"], apk_info["versionCode"])
    # print(title)


