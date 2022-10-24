# @charset "utf-8"
import os
import sys
import requests
from xml.etree import ElementTree
from functools import cmp_to_key
import zipfile

driver_list = [
    'chrome',
    ]

#====================================================================
# chrome
#====================================================================
def update_chrome(basepath, version):
    def compare(a, b, depth):
        sa = a.split('.')
        sb = b.split('.')

        for i in range(depth):
            if int(sa[i]) < int(sb[i]):
                return -1
            if int(sa[i]) > int(sb[i]):
                return 1
        return 0

    def ver_compare_depth4(a, b):
        return compare(a, b, 4)

    def ver_compare_depth3(a, b):
        return compare(a, b, 3)

    def ver_compare_depth2(a, b):
        return compare(a, b, 2)

    def ver_compare_depth1(a, b):
        return compare(a, b, 1)

    res = requests.get('https://chromedriver.storage.googleapis.com/?delimiter=/&prefix=')
    if res.status_code != 200:
        print(driver + ':url get error')
    xml = ElementTree.fromstring(res.content)
    prefix = xml.tag.replace('ListBucketResult', '')

    ver_list = []
    for node in xml.iter(prefix+'CommonPrefixes'):
        for item in node.iter(prefix+'Prefix'):
            ver_list.append(item.text.replace('/', ''))
    ver_list = list(filter(lambda x: x.split('.')[0].isdecimal(), ver_list))
    ver_list = sorted(ver_list, key=cmp_to_key(ver_compare_depth4), reverse=True)
    select_versions = list(filter(lambda x: ver_compare_depth3(version, x)<=0, ver_list))
    if len(select_versions) <= 0:
        select_versions = list(filter(lambda x: ver_compare_depth2(version, x)<=0, ver_list))
    if len(select_versions) <= 0:
        select_versions = list(filter(lambda x: ver_compare_depth1(version, x)<=0, ver_list))
    if len(select_versions) <= 0:
        select_versions = [ver_list[0]]
    else:
        select_versions = list(filter(lambda x: ver_compare_depth4(version, x)>=0, select_versions))
        if len(select_versions) <= 0:
            select_versions = [ver_list[0]]
        else:
            select_version = select_versions[0]
    print(select_version)

    zip = requests.get('https://chromedriver.storage.googleapis.com/' + select_version + '/chromedriver_win32.zip')

    # ダウンロードしたZIPファイルの書き出し
    with open(basepath + '\\' + select_version + '_chromedriver_win32.zip', 'wb') as f:
        for chunk in zip.iter_content():
            f.write(chunk)

    # ZIPファイルの解凍
    with zipfile.ZipFile(basepath + '\\' + select_version + '_chromedriver_win32.zip') as f:
        f.extractall(basepath)

#====================================================================
# main
#====================================================================
def main():
    if len(sys.argv) != 2:
        print('webdriverを書き出すパスを引数に指定してください')
        sys.exit()
    basepath = os.path.abspath(sys.argv[1])
    for driver in driver_list:
        with open(driver+'.ver', 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
            globals()['update_'+driver](basepath, lines[0])

if __name__ == '__main__':
    main()

