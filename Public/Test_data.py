#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


def download_apk(folder='../apk/'):
    html = requests.get('http://www1.xiaoying.co/Android/vivavideo/vivavideo_install.html')
    soup = BeautifulSoup(html.text, "lxml")
    tmp = soup.find(href=re.compile("xiaoyingtest"))
    apk = (tmp.get('href'), tmp.text)   # apk的下载链接和文件名
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        pass
    r = requests.get(apk[0], 'wb')
    print('from %s \ndownloading  %s ' % (apk[0],  apk[1]))
    if r.status_code == 200:
        with open("%s/%s" % (folder, apk[1]), "wb") as code:
            code.write(r.content)
        return folder+apk[1]
    else:
        print('%s \nCannot GET ' % r.url)


if __name__ == '__main__':
    # print(get_apk_url())
    # html = requests.get(url)
    # soup = BeautifulSoup(html.text,"lxml")
    # apk = soup.find(href=re.compile("xiaoyingtest"))
    # print(apk.text)
    # apk_url = apk.get('href')
    # print(apk_url)
    print(download_apk())



