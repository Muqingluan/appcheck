
import urllib2
import sys,os
import json
import time


def store(path,data):
    with open(path + '/savedata.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def load(path):
    with open(path + '/savedata.json') as json_file:
        data = json.load(json_file)
        return data


def yingyongbaodownload(path):

    print "save path is " + path
    apkfile_store = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

    if os.path.exists(path + '/savedata.json'):
        apkfile_store = load(path)

    gameCategory = [147, 121, 149, 144, 151, 148, 153, 146]

    urlarrary = []

    for i in range(122):
        if i < 100:
            continue
        url = "http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=" + str(i) + "&pageSize=60&pageContext=0"
        urlarrary.append(url)

    for i in range(len(gameCategory)):
        url = 'http://android.myapp.com/myapp/cate/appList.htm?orgame=2&categoryId='+ str(gameCategory[i]) +'&pageSize=60&pageContext=0'
        urlarrary.append(url)

    for i in urlarrary:

        print "main url is " + i

        req = urllib2.Request(i,headers=headers)


        response = urllib2.urlopen(req)

        parserjson = json.loads(response.read())
        if parserjson is None:
            continue
        #print parserjson

        time.sleep(1)

        count = parserjson[u'count']
        print "this apk count is " + str(count)
        for i in range(count - 1):
            #time.sleep(1)
            if parserjson[u'obj'] is None or len(parserjson[u'obj']) == 0 or parserjson[u'obj'] == 'null':
                continue
            if parserjson[u'obj'][i] is None:
                continue
            if parserjson[u'obj'][i][u'apkUrl'] is None:
                continue
            print parserjson[u'obj'][i][u'apkUrl']
            downloadurl = parserjson[u'obj'][i][u'apkUrl']

            apkfile_name = path + str(downloadurl).split('=')[1].split('&')[0]
            print apkfile_name + "kiwisec"
            if apkfile_name in apkfile_store:
                continue
            apkfile = urllib2.urlopen(downloadurl)
            data = apkfile.read()
            with open(apkfile_name, "wb") as code:
                code.write(data)

            apkfile_store.append(apkfile_name)
            store(path,apkfile_store)

